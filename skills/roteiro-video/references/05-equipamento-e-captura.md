# 05. Equipamento e captura

## Índice
1. Inventário e lacunas
2. iPhone 17 Pro: lentes
3. Blackmagic Camera: presets
4. LOG: quando usar e como expor
5. Tremulação de luz no Brasil (60 Hz)
6. Cor e exportação
7. Áudio
8. Tripé e movimento
9. Ray-Ban Meta
10. Carro
11. Estúdio: montagem do set
12. Compras por prioridade

---

## 1. Inventário e lacunas

| Tem | Nível |
|---|---|
| iPhone 17 Pro | Câmera de cinema de bolso: três câmeras de 48 MP, ProRes, ProRes RAW, Apple Log 2 |
| Blackmagic Camera (app) | Controle manual total: shutter em ângulo, ISO, balanço de branco, foco, zebra, false color, LUT de preview |
| Tripé | Base de toda fala |
| Microfone profissional | Voz limpa |
| Ray-Ban Meta | POV sem mãos |
| Carro | Mobilidade pra locação e deslocamento como narrativa |
| Estúdio | Set principal |

**Lacunas, em ordem de impacto** (conselheiro brutal)
1. **Luz.** Nenhuma fonte de luz controlada no inventário. LOG em ambiente com pouca luz gera ruído que nenhum tratamento salva. É a maior diferença entre "vídeo de celular" e "vídeo de produtora".
2. **Tratamento acústico.** Microfone bom em sala com eco grava eco bom.
3. **Filtro ND.** Sem ele, em externa com sol, o shutter vai a 1/1000 ou mais e o movimento fica picotado, sem cara de cinema.
4. **SSD externo.** ProRes enche o iPhone em minutos e exige SSD em frame rate alto.
5. **Estabilizador (gimbal) ou slider.** Sem ele, todo movimento real depende de mão firme.

## 2. iPhone 17 Pro: lentes

| Lente | Equivalente | Uso |
|---|---|---|
| Ultra-angular 0,5x | 13 mm | Escala, ambiente inteiro, plano "IMAX", macro de detalhe |
| Principal 1x | 24 mm | Plano geral e médio, B-roll, pouca luz (melhor sensor) |
| Principal 2x | 48 mm (recorte do sensor de 48 MP) | **Fala padrão.** Rosto sem distorção a ~1,2-1,5 m |
| Tele 4x | 100 mm | Close bonito, fundo comprimido e desfocado, detalhe à distância |
| Tele 8x | 200 mm (recorte do tele) | Compressão extrema em externa. Qualidade cai em vídeo, testar antes |

- Rosto com 1x de perto distorce (nariz grande). Pra fala, 2x ou 4x com a câmera mais longe.
- O tele precisa de mais luz. Em estúdio escuro, o iPhone pode trocar sozinho pra recorte da principal.
- Câmera frontal (18 MP, Center Stage) só pra emergência ou bastidor. A traseira é muito superior.
- Dual Capture (app Câmera da Apple) grava frontal e traseira ao mesmo tempo: útil pra reação + tela, sem LOG.

## 3. Blackmagic Camera: presets

Gravar sempre em **4K vertical**. Escolher um frame rate padrão do perfil e manter.

| Preset | Resolução / fps | Shutter | Codec | Uso |
|---|---|---|---|---|
| A. Estúdio fala | 4K / 24 | 144° (1/60) | HEVC 10 bits, Apple Log | Fala diária, peso leve |
| A+. Estúdio hero | 4K / 24 | 144° (1/60) | ProRes 422 HQ, Apple Log, em SSD | Vídeo principal da semana, máximo de cor |
| B. Externa com sol | 4K / 24 | 180° (1/48) com ND | HEVC ou ProRes, Apple Log | Parque, Serra, rua |
| C. Slow motion | 4K / 120 | 360° (1/120) sob luz artificial, 180° (1/240) no sol | HEVC, Apple Log | Clímax, detalhe, impacto |
| D. Rápido sem pós | 4K / 24 ou 30 | 180° | HEVC, sem LOG (Rec.709) | Bastidor, trend, quando não vai ter tempo de tratar cor |

Configurações fixas em todos
- ISO travado (nunca automático). O LOG da Apple se comporta mal com ISO variando.
- Balanço de branco travado: 5600 K luz do dia, 3200 K tungstênio, ou o valor das luzes do estúdio.
- Foco travado nos olhos (fala) ou ponto marcado (detalhe). Focus peaking ligado.
- LUT de preview Apple Log → Rec.709 ligado só na tela, sem gravar no clipe.
- Estabilização desligada ou mínima no tripé; ligada na mão.
- Áudio externo selecionado e medidor visível na tela.
- Celular em modo avião, notificações desligadas, brilho da tela no máximo pra julgar exposição.

Sobre ProRes RAW: o 17 Pro grava, mas pra Reels é exagero. O Instagram recomprime tudo pra 1080x1920. O custo de armazenamento e de fluxo de trabalho não volta em qualidade visível no feed. Reservar pra projeto de cliente ou peça que vai pra tela grande.

Armazenamento aproximado por minuto em 4K/24: ProRes 422 HQ ~5 GB, ProRes 422 ~3,5 GB, HEVC 10 bits ~0,5 a 1 GB.

## 4. LOG: quando usar e como expor

- **Usar** quando a edição vai ter etapa de cor. LOG guarda mais informação de luz e sombra, e a cor se molda na pós.
- **Não usar** quando o vídeo sai no mesmo dia sem tratamento. LOG sem grade sai cinza e lavado no feed. Usar o preset D.
- Expor olhando o preview com LUT: pele bem exposta, nada importante estourado (janela, céu, tela).
- Na dúvida, 1/3 a 2/3 de stop mais claro que o normal. O ruído do LOG aparece nas sombras; clarear na captura e escurecer na pós limpa a imagem.
- Usar false color e zebra do app pra conferir altas luzes antes de cada take.
- Cada setup novo: gravar 3 s de um cartão branco ou cinza na luz da cena. Facilita casar a cor na edição.

## 5. Tremulação de luz no Brasil (60 Hz)

A rede elétrica brasileira é 60 Hz. Lâmpadas e LEDs baratos piscam 120 vezes por segundo. Com shutter errado aparecem faixas e piscadas na imagem.

| Frame rate | Shutter sem tremulação | Observação |
|---|---|---|
| 24 fps | 144° (1/60) | Padrão estúdio. 180° (1/48) pode piscar |
| 30 fps | 180° (1/60) | Seguro |
| 60 fps | 360° (1/60) ou 180° (1/120) | 1/120 é o mais usado |
| 120 fps | 360° (1/120) | Slow motion em estúdio |

- Luz do dia não pisca. Em externa, 180° normal.
- Painel de LED de vídeo de boa qualidade não pisca; lâmpada de casa e fita de LED barata, sim. Testar gravando 5 s antes do take.

## 6. Cor e exportação

Fluxo de cor
1. DaVinci Resolve (gratuito) ou CapCut com LUT importado.
2. Converter Apple Log pra Rec.709: LUT oficial da Apple ou transformação de espaço de cor (Color Space Transform) no Resolve. Usar o perfil correspondente ao LOG gravado (Apple Log ou Apple Log 2).
3. Corrigir exposição e balanço de branco.
4. Aplicar look: contraste, P&B da marca, ou dois códigos (P&B no problema, cor no resultado).
5. Conferir pele no vetorscópio (linha de pele).

Exportação
- 1080x1920, 9:16, mesmo frame rate da timeline.
- H.264 ou HEVC, bitrate alto (20-30 Mbps). O Instagram recomprime de qualquer jeito.
- **SDR Rec.709.** O tratamento de HDR no Instagram é inconsistente: o vídeo pode sair estourado ou apagado em parte dos aparelhos.
- No Instagram, ativar a opção de envio na qualidade mais alta (Configurações, qualidade de mídia). Subir no Wi-Fi.

## 7. Áudio

Regras gerais
- 48 kHz. Picos entre -12 e -6 dB na gravação (sobra espaço pra grito ou risada sem estourar).
- Se o microfone tiver gravação interna de segurança (backup), ligar sempre.
- Fone de ouvido monitorando o primeiro take de cada setup.
- Gravar 10 s de ambiente (room tone) em cada locação, sem ninguém falar.
- Áudio gravado separado do vídeo: bater uma palma no começo do take pra sincronizar.
- O Blackmagic Camera aceita microfone externo pela USB-C e mostra os níveis na tela.

Posição por tipo de microfone

| Tipo | Posição | Atenção |
|---|---|---|
| Lapela sem fio | 15-20 cm abaixo do queixo, centralizada, escondida ou assumida | Roupa raspando no mic; protetor de vento em externa |
| Shotgun (direcional) | 30-60 cm acima da cabeça, fora do quadro, apontado pra boca | Pega eco da sala; pior em sala vazia |
| Dinâmico de estúdio | 5-10 cm da boca | Aparece no quadro; bom pra formato podcast |
| Condensador de estúdio | 15-30 cm | Pega tudo da sala; só em sala tratada |

Acústica do estúdio (barato, resolve 80%)
- Eco mata mais que ruído de fundo. Bater palma: se "canta", tem eco.
- Tapete no chão, cortina pesada, sofá, estante cheia de livros.
- Edredom ou cobertor atrás da câmera (a parede pra onde a voz vai primeiro).
- Desligar ar-condicionado, ventilador e geladeira próxima durante o take.

## 8. Tripé e movimento

- Altura da lente: na linha dos olhos pra fala neutra; um pouco abaixo pra autoridade.
- Plano travado é o melhor amigo do jump cut: cortes na fala ficam limpos com punch-in alternado.
- Pan e tilt só se a cabeça do tripé for fluida. Movimento travando no meio estraga o plano.
- Time-lapse no tripé: pôr do sol, chegada no estúdio, tela mudando.
- Movimento sem gimbal: iPhone nas duas mãos, cotovelos colados no corpo, passos curtos com o joelho flexionado ("andar de ninja"), estabilização ligada.
- Push-in falso: zoom digital lento na edição, em 4K com folga pra 1080. Funciona pra fala; não cria paralaxe.

## 9. Ray-Ban Meta

| | Gen 1 (2023) | Gen 2 (2025) |
|---|---|---|
| Vídeo | 1080p a 30 fps | 3K a 30 fps, 1440p a 30 fps, 1200p a 60 fps |
| Clipe | Até 60 s (estendido pra 3 min no app em atualização) | Até 3 min |
| Modos extras | Não | Hyperlapse e câmera lenta |
| Orientação | Vertical | Vertical |

Conferir qual geração o Eric tem.

Onde encaixa no roteiro
- **Confirmação do clique:** POV caminhando até o desafio, abrindo a porta do cliente, olhando a pilha de pedidos.
- **Escalada:** mãos digitando, montando, testando. O espectador vê pelos olhos do Eric.
- **Montagem paralela:** POV como linha visual própria (textura diferente separa as linhas).
- **Bastidor real:** captura sem câmera na cara, reação espontânea do cliente.
- **Hyperlapse:** deslocamento até a locação.

Regras de gravação
- A cabeça é o tripé. Mover o corpo, não a cabeça. Virar a cabeça devagar.
- Olhar fixo no objeto 2 s antes e 2 s depois da ação. Dá ponto de corte.
- Mãos na metade de baixo do campo de visão: a lente pega mais largo do que parece.
- Sem LOG, compressão maior, faixa dinâmica menor: evitar contraluz forte.
- A voz de quem usa sai razoável pelos microfones da armação; voz principal continua no microfone profissional.
- Na timeline de 24 fps, o material de 30 fps do óculos dá uma leve trepidação. Aceitável em POV; evitar em movimento lento.
- O LED de gravação acende. Avisar quem estiver na cena. Não filmar tela de cliente com dado pessoal sem autorização (LGPD).

## 10. Carro

- **Narrativa:** deslocamento é dificuldade visível. "Fui até o cliente" vira estrada, painel, chegada.
- **Locação:** o carro parado é um estúdio de fala razoável (quadro dentro do quadro pelo para-brisa, luz lateral da janela). Motor e ar desligados pro áudio.
- **Planos:** suporte no para-brisa ou painel apontando pro motorista; câmera do lado de fora com o carro andando devagar em rua vazia (passageiro filma); POV do Ray-Ban no banco do passageiro.
- **Segurança e lei:** nunca falar com a câmera, mexer no celular ou conferir take dirigindo. Manusear celular ao volante é infração gravíssima no Código de Trânsito. Fala no carro: parado ou com outra pessoa dirigindo.

## 11. Estúdio: montagem do set

Planta básica (vista de cima)
```
            [fundo com profundidade: estante, planta, luz prática]
                         (1,5 a 2 m)
   [contraluz]          EU (sujeito)          [pano preto: negative fill]
        \                    |
   [luz principal 45°]   [mic fora do quadro]
                             |
                  [iPhone 2x no tripé, ~1,2-1,5 m]
           [cobertor ou cortina atrás da câmera]
```

Regras do set
- Sujeito longe da parede (1,5 a 2 m): fundo desfoca e a sombra não bate na parede.
- Fundo um stop mais escuro que o rosto, com uma luz prática (abajur ou LED quente).
- Elemento da marca NADA no fundo, sutil: objeto P&B, quadro, tipografia. Nunca logo gigante.
- Parede lisa branca de frente = cara de vídeo amador. Girar o set pra pegar a diagonal do cômodo.
- Bancada separada pra inserts de cima (top-down) e por cima do ombro na tela.
- Roteiro na tela do notebook logo abaixo da lente, ou teleprompter, pra manter o olhar na câmera.

## 12. Compras por prioridade

| Prioridade | Item | Por que |
|---|---|---|
| 1 | Luz LED de vídeo tipo COB (60 a 150 W, luz do dia, alto IRC) + softbox grande ou lanterna | Luz principal. Maior salto de qualidade possível |
| 2 | Luz de fundo: tubo de LED RGB ou luminária prática quente | Profundidade e separação |
| 3 | Tratamento acústico: cobertores pesados, painéis, tapete | Voz de estúdio |
| 4 | Filtro ND variável (2 a 5 stops) com suporte pro iPhone | Shutter de cinema em externa |
| 5 | SSD USB-C rápido + cabo 10 Gbps | ProRes sem encher o iPhone |
| 6 | Gimbal pra celular | Push-in, travelling, dolly zoom |
| 7 | Rebatedor 5 em 1 | Externa, preenchimento barato |
| 8 | Teleprompter de câmera traseira | Olho na lente sem decorar |

Escolher marcas e preços na hora da compra; o mercado muda rápido.
