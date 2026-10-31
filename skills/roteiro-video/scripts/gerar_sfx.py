#!/usr/bin/env python3
"""Gera os efeitos sonoros da skill (sintetizados do zero, livres de direitos).

Uso: python3 gerar_sfx.py [pasta_saida]
Saida padrao: ../assets/sfx  (WAV 48 kHz, 16 bit, mono)

Arquivos:
  shepard_subida_12s.wav        tom de Shepard subindo (tensao infinita, Dunkirk)
  tique_taque_acelerando_10s.wav relogio que acelera (prazo, Dunkirk/Interstellar)
  sub_drop_3s.wav               impacto grave pro climax ou revelacao
  braam_4s.wav                  "BRAAAM" de trailer (A Origem)
"""
import sys
import wave
from pathlib import Path

import numpy as np

SR = 48000
rng = np.random.default_rng(7)


def salvar(nome, x, pasta):
    x = np.asarray(x, dtype=np.float64)
    x = x / (np.max(np.abs(x)) + 1e-12) * 0.89  # pico ~ -1 dBFS
    pcm = (x * 32767).astype("<i2")
    caminho = pasta / nome
    with wave.open(str(caminho), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print(f"ok {caminho} ({len(x) / SR:.1f}s)")


def fade(x, ini=0.01, fim=0.05):
    n_i, n_f = int(ini * SR), int(fim * SR)
    env = np.ones_like(x)
    if n_i:
        env[:n_i] = np.linspace(0, 1, n_i)
    if n_f:
        env[-n_f:] = np.linspace(1, 0, n_f)
    return x * env


def shepard(dur=12.0, oitavas=8, f_min=40.0, vel=0.22):
    t = np.arange(int(dur * SR)) / SR
    out = np.zeros_like(t)
    for k in range(oitavas):
        p = (k + vel * t) % oitavas               # posicao em oitavas
        f = f_min * 2.0 ** p
        amp = 0.5 * (1 - np.cos(2 * np.pi * p / oitavas))  # some nas pontas
        fase = 2 * np.pi * np.cumsum(f) / SR
        out += amp * np.sin(fase)
    cresc = np.linspace(0.35, 1.0, len(t)) ** 1.6   # crescendo de riser
    return fade(out * cresc, 1.0, 0.08)


def tique_taque(dur=10.0, bpm_ini=60.0, bpm_fim=210.0):
    n = int(dur * SR)
    out = np.zeros(n)
    t, i = 0.0, 0
    while t < dur - 0.05:
        frac = t / dur
        bpm = bpm_ini * (bpm_fim / bpm_ini) ** frac
        f = 3100.0 if i % 2 == 0 else 2350.0       # tique / taque
        m = int(0.06 * SR)
        tt = np.arange(m) / SR
        clique = rng.standard_normal(m) * np.exp(-tt / 0.0015)
        corpo = np.sin(2 * np.pi * f * tt) * np.exp(-tt / 0.012)
        grave = 0.5 * np.sin(2 * np.pi * 620 * tt) * np.exp(-tt / 0.02)
        s = int(t * SR)
        seg = (0.35 * clique + corpo + grave)[: n - s]
        out[s : s + len(seg)] += seg * (0.6 + 0.4 * frac)
        t += 60.0 / bpm
        i += 1
    return fade(out, 0.0, 0.05)


def sub_drop(dur=3.0, f_ini=130.0, f_fim=28.0):
    t = np.arange(int(dur * SR)) / SR
    f = f_fim + (f_ini - f_fim) * np.exp(-t / 0.45)
    fase = 2 * np.pi * np.cumsum(f) / SR
    corpo = np.sin(fase) * np.exp(-t / 1.1)
    m = int(0.03 * SR)
    trans = np.zeros_like(t)
    ruido = rng.standard_normal(m) * np.exp(-np.arange(m) / SR / 0.004)
    trans[:m] = np.convolve(ruido, np.ones(24) / 24, mode="same")  # passa-baixa simples
    return fade(np.tanh(1.8 * (corpo + 0.6 * trans)), 0.0, 0.2)


def braam(dur=4.0):
    t = np.arange(int(dur * SR)) / SR
    env = np.minimum(t / 0.12, 1.0) * np.exp(-np.maximum(t - 0.6, 0) / 1.4)
    corte = 250 + 1400 * np.minimum(t / 0.25, 1.0) * np.exp(-t / 1.6)  # brilho abre e fecha
    vib = 1 + 0.003 * np.sin(2 * np.pi * 5.2 * t)
    out = np.zeros_like(t)
    for f0 in (55.0, 82.41, 110.0):
        for det in (0.997, 1.003):
            base = f0 * det * vib
            fase0 = 2 * np.pi * np.cumsum(base) / SR
            n_harm = int(4000 // f0)
            for h in range(1, n_harm + 1):
                peso = (1.0 / h) * np.exp(-(h * f0) / corte)
                out += peso * np.sin(h * fase0)
    return fade(np.tanh(1.2 * out / np.max(np.abs(out))) * env, 0.0, 0.3)


if __name__ == "__main__":
    pasta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "assets" / "sfx"
    pasta.mkdir(parents=True, exist_ok=True)
    salvar("shepard_subida_12s.wav", shepard(), pasta)
    salvar("tique_taque_acelerando_10s.wav", tique_taque(), pasta)
    salvar("sub_drop_3s.wav", sub_drop(), pasta)
    salvar("braam_4s.wav", braam(), pasta)
