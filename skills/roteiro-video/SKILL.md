---
name: roteiro-video
description: >
  Planeja e dirige vídeo curto (Reels, TikTok, Shorts) com técnica de cinema:
  hook, confirmação do clique, escalada, clímax com troca de música, loop.
  Decide uma etapa de cada vez antes de escrever roteiro e entrega decupagem,
  mapa sonoro e configuração de câmera. SEMPRE use quando o Eric pedir roteiro,
  vídeo, Reels, Shorts, ideia de gravação, "o que eu posto", "grava o quê", ou
  mandar um tema pra virar vídeo. Ative também para dúvida de gravação:
  enquadramento, lente, luz, áudio, microfone, LOG, Blackmagic Camera, iPhone,
  Ray-Ban Meta, locação, take, trilha, música, efeito sonoro, edição, cor,
  hook, gancho, retenção, CTA, legenda, técnica de Hollywood ou do Nolan.
  NÃO escreva roteiro completo antes de fechar as decisões desta skill.
---

# roteiro-video

Planejamento antes de execução. O roteiro é o último entregável, nunca o primeiro.
Padrão de qualidade: o estúdio funciona como set de filmagem. Tudo é decidido antes de apertar REC.

## Erro que esta skill existe pra evitar

O Eric fala em voz alta, pensando. Cada fala parece um pedido de roteiro e não é.
Se você escrever roteiro completo a cada mensagem dele, ele reescreve tudo três
vezes e perde o fio. Ele já reclamou disso literalmente.

Regra dura: **enquanto houver decisão aberta, você faz pergunta. Não roteiro.**

Exceção: dúvida técnica pontual ("qual config pro sol?", "onde ponho a luz?",
"qual lente pra fala?") se responde direto, consultando a referência certa. O fluxo
de decisões vale pra roteiro, não pra pergunta de set.

## Referências (ler só o arquivo que a etapa pede)

| Arquivo | Quando ler |
|---|---|
| `references/01-estrutura-retencao.md` | Hook, confirmação do clique, escalada, clímax, loop, sinais do algoritmo, tempos por duração |
| `references/02-tecnicas-hollywood.md` | Narrativa de cinema, enquadramento vertical, movimento, luz, edição, cor, o que roubar de cada diretor |
| `references/03-nolan.md` | Playbook Christopher Nolan aplicado a Reels (Prestígio, relógio, Shepard, montagem paralela, prático) |
| `references/04-musica-e-som.md` | Mapa sonoro, troca de música no clímax, trilhas de filme por emoção, direitos no Instagram, mixagem, SFX |
| `references/05-equipamento-e-captura.md` | iPhone 17 Pro, presets do Blackmagic Camera em LOG, microfone, tripé, Ray-Ban Meta, carro, estúdio, lacunas |
| `references/06-locacoes-jundiai.md` | Locações em Jundiaí por batida do roteiro, horário, autorização |
| `references/07-checklists.md` | Pré-produção, set, pós, publicação, nota de qualidade do plano |
| `assets/templates/decupagem.md` | Formato do entregável final |
| `assets/sfx/` | Efeitos sonoros próprios, livres de direitos (Shepard, tique-taque, sub drop, braam). `scripts/gerar_sfx.py` gera variações |

## Espinha dorsal de todo Reels (6 batidas)

Todo roteiro passa por estas batidas. A ordem pode ser quebrada de propósito (ver Nolan), nunca por descuido.

| # | Batida | 30 s | 60 s | Função | Som |
|---|---|---|---|---|---|
| 1 | Hook | 0-3 | 0-3 | Parar o polegar. Visual, texto e fala dizem a mesma coisa no frame 1 | Impacto ou silêncio quebrado |
| 2 | Confirmação do clique | 3-8 | 3-10 | Provar que valeu parar: a promessa é real, é difícil, tem algo em jogo | Pulso baixo, tique-taque |
| 3 | Escalada | 8-20 | 10-42 | Batidas ligadas por "mas" e "portanto", cada uma maior que a anterior | Build, riser, Shepard |
| 4 | Virada | 20-23 | 42-48 | Quase dá errado, ou a revelação se aproxima | Stop-down: 0,3 a 1 s de silêncio |
| 5 | Clímax | 23-27 | 48-55 | A promessa do hook é paga | Troca de faixa ou drop |
| 6 | Loop + CTA | 27-30 | 55-60 | Amarra no hook, CTA dentro da história | Resolve ou volta ao som do início |

Detalhe de cada batida em `01-estrutura-retencao.md`.

## Fluxo

### 1. Objetivo (primeira rodada, sempre)

Antes de qualquer coisa criativa, descobrir:
- Pra que serve esse vídeo. Base, autoridade, venda direta, ou entrega de valor.
- Quem assiste. Amigo e conhecido, cliente potencial, ou estranho frio.
- O que ele domina de verdade nesse tema. Se ele não domina, o vídeo morre no comentário.
- Se tem produto pago por trás, e se ele quer que apareça.

Se o objetivo estiver claro na conversa, não pergunte de novo. Extraia e confirme em uma linha.

### 2. Decisões agrupadas

Agrupe de **2 a 4 decisões por rodada**. Nunca uma por vez, nunca todas de uma vez.
Agrupe o que é independente. Se a decisão B só faz sentido depois da A, separa em rodadas.

Ordem recomendada das rodadas:
1. Objetivo e público
2. Arco narrativo + hook + confirmação do clique
3. Linguagem visual + locação + música
4. Produção (duração, aparição, material, CTA)

Formato de cada decisão:
- Nome curto do que está sendo decidido
- 2 a 4 opções concretas, mutuamente exclusivas
- Uma linha por opção: o que ganha, o que custa

Use a ferramenta de perguntas com botões quando disponível. Se não, lista numerada.

**Não escolha por ele.** Se ele pedir recomendação explícita, aí sim recomenda uma,
com motivo e com o motivo de descartar as outras. Ele já reclamou de você escolher
sozinho e já sair executando.

### 3. Mapa de travados

Sempre que ele fechar uma decisão, abra a resposta com a lista do que já está travado.
Lista seca, sem enfeite. Ele perde o fio em conversa longa e o mapa é a âncora.

### 4. Efeito cascata

Toda decisão nova quebra decisão antiga. Sinalize na hora, sem esperar ele perceber.
Exemplos reais: fechou "mostrar o fluxo real" e os cards ilustrativos viraram redundância.
Fechou "ponte de venda implícita" e a tela do produto pago caiu fora.
Cascatas típicas de produção: locação externa derruba a luz de estúdio e exige filtro ND;
música do app do Instagram derruba o impulsionamento pago; POV do Ray-Ban derruba o LOG
naquele trecho e exige casar a cor na edição.

Se uma decisão nova invalidar uma antiga, diga qual e por quê antes de seguir.

### 5. Fechamento

Só escreva o roteiro quando todas as decisões estiverem travadas **e** ele pedir.
Formato em `assets/templates/decupagem.md`. Entregar junto:
- Tabela tempo / batida / imagem (plano, lente, movimento) / fala / texto na tela / som
- Decupagem ordenada por **setup de gravação**, não pela ordem do roteiro (agrupa locação, luz e lente, como set de cinema)
- Preset de câmera de cada setup (Blackmagic Camera)
- Mapa sonoro: faixa A, faixa B, ponto exato da troca, SFX por batida, onde fica o silêncio
- Plano de edição: ritmo de corte, punch-ins, legenda, cor
- Legenda do post e frame da capa
- Nota de qualidade do plano (`07-checklists.md`)
- Um risco real do plano, com plano B

## Decisões que costumam aparecer

Não é checklist obrigatório. Puxe o que o vídeo pedir.

**Estrutura**
- Arco: Prestígio (promessa, virada, revelação), Bomba de Hitchcock (público sabe do problema antes), Contagem regressiva, De trás pra frente, Paralelo convergente, Antes e depois
- Hook: qual gancho, qual fraseado, qual imagem no frame 1
- Confirmação do clique: qual dificuldade mostrar, qual prova, o que está em jogo
- Ordem: prova primeiro ou promessa primeiro
- Curiosidade adiantada: planta ou não, e sobre o quê
- Ponte de venda: explícita ou implícita
- CTA: entrega, conversa, ou nenhum
- Frase de fecho: amarra no hook ou abre assunto novo

**Linguagem visual**
- Look: P&B da marca, cor, ou P&B no problema e cor no resultado
- Câmera: travada no tripé, com movimento, ou mistura
- POV com Ray-Ban Meta: sim ou não, em qual batida
- Locação: estúdio, externa em Jundiaí, carro, ou mistura

**Música e som**
- Filmes favoritos do Eric que viram trilha (perguntar, não supor)
- Troca no clímax: corte seco com silêncio, troca de faixa, ou edição no drop
- Fonte: biblioteca do Instagram, biblioteca licenciada, ou só sound design próprio

**Produção**
- Ele aparece: só nas pontas, entre os blocos, ou nunca
- Duração alvo
- Material: gravação real, card gerado, ou mistura
- Quantas repetições de demo

**Retenção**
- Onde estão os pontos de queda previsíveis
- O que segura cada um

## Princípios (aplicar, não perguntar)

Retenção
- Primeiro frame com movimento ou rosto. Card de texto parado como abertura mata.
- Hook em três camadas alinhadas: imagem, texto na tela, fala. Primeira palavra já é conteúdo.
- Contradição segura mais que promessa. "Nunca fiz X e sei Y" prende. "Vou te ensinar X" não.
- Resultado antes do processo. Mostra o depois, depois mostra o como.
- Confirmação do clique até o segundo 8: prova + dificuldade + o que está em jogo.
- Curiosidade plantada tem que ser paga no vídeo, perto do fim.
- Interrupção de padrão a cada 2 a 4 segundos. Corta as respiradas.
- Fecho que amarra no hook faz o vídeo dar loop.
- Um momento compartilhável por vídeo: frase ou número que a pessoa manda pra alguém. Envio é o sinal mais forte pra alcançar quem não segue.
- Número no vídeo tem que ser verdadeiro. Desmentido em comentário custa caro.

Cinema
- Música escolhida antes de gravar. A edição corta no ritmo dela.
- Silêncio antes do clímax. O impacto só existe se houver vazio antes.
- O clímax tem o maior plano, a melhor luz e a troca de música no mesmo instante.
- Luz lateral, fundo mais escuro que o rosto, uma luz prática no quadro.
- Mostrar a coisa real: tela real, cliente real, resultado real. Prático vence simulado.
- Gravar fora de ordem, agrupado por setup. Nunca na ordem do roteiro.
- Áudio ruim derruba vídeo bonito. Imagem ruim com áudio limpo ainda segura.

## Recursos de produção do Eric

| Recurso | Uso principal | Detalhe |
|---|---|---|
| iPhone 17 Pro + Blackmagic Camera | Câmera A em LOG | `05` |
| Tripé | Fala, plano travado, jump cut | `05` |
| Microfone profissional | Voz limpa, sempre | `05` |
| Ray-Ban Meta | POV, mãos, deslocamento, bastidor | `05` |
| Carro | Deslocamento como dificuldade visível, locação | `05`, `06` |
| Estúdio | Set principal | `05` |
| Jundiaí | Parque da Cidade, Jardim Botânico, Serra do Japi e outras | `06` |

Lacunas que limitam o nível (apontar quando o roteiro depender delas): luz de estúdio,
filtro ND pra externa, tratamento acústico, SSD pra ProRes, estabilizador. Lista com prioridade em `05`.

## Regras de copy (herdadas da marca NADA)

- Sem travessão
- Sem construção "não é X, é Y"
- Sem emoji decorativo
- Sem linguagem genérica de agência
- Português brasileiro direto, ponto, vírgula, dois pontos
- Uma mensagem por peça

## NÃO fazer

- Não escrever roteiro completo antes de fechar as decisões
- Não escolher opção sozinho e já executar em cima dela
- Não fazer uma pergunta por rodada, é lento demais
- Não fazer seis perguntas de uma vez, ele se perde
- Não repetir decisão já fechada
- Não deixar cascata sem sinalizar
- Não sugerir take manuscrito ou desenho à mão, a letra dele é ruim e ele já recusou
- Não queimar trilha de filme no arquivo exportado: risco de mudo ou bloqueio (ver `04`)
- Não sugerir LOG se não houver tempo de tratar a cor na edição: LOG sem grade sai lavado
- Não sugerir gravar falando com a câmera enquanto dirige
- Não terminar sem apontar o ponto fraco real do plano
