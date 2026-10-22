# Leituras · IA aplicada

## 1. Como funciona um LLM (tokens, transformers, treinamento)

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [LLM Course (versão em português)](https://huggingface.co/learn/llm-course/pt/chapter1/1) | Hugging Face | Curso | PT-BR | Grátis | Transformers, tokenizadores e ajuste fino com código, com capítulos traduzidos. |
| 2 | [Transformers: funcionamento e benefícios](https://www.alura.com.br/artigos/transformers) | Alura | Artigo | PT-BR | Grátis | Resumo em português da arquitetura por trás dos LLMs. |
| 3 | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Jay Alammar | Guia | EN | Grátis | A explicação visual mais citada de como a atenção funciona. |
| 4 | [What Is ChatGPT Doing … and Why Does It Work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) | Stephen Wolfram | Artigo | EN | Grátis | Texto longo que vai da probabilidade da próxima palavra até o treinamento. |
| 5 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Vaswani et al. (Google) | Artigo científico | EN | Grátis | O artigo de 2017 que criou o transformer. Leia depois dos guias. |

## 2. Engenharia de prompt e de contexto

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Visão geral da engenharia de prompts](https://platform.claude.com/docs/pt-BR/build-with-claude/prompt-engineering/overview) | Anthropic | Documentação | PT-BR | Grátis | Guia oficial com as técnicas que mais funcionam, em português. |
| 2 | [Guia de Engenharia Prompt](https://www.promptingguide.ai/pt) | DAIR.AI | Guia | PT-BR | Grátis | Catálogo de técnicas de prompt com exemplos, traduzido para o português. |
| 3 | [Engenharia de Contexto para Agentes de IA](https://github.com/microsoft/ai-agents-for-beginners/tree/main/translations/pt-BR/12-context-engineering) | Microsoft (AI Agents for Beginners) | Curso | PT-BR | Grátis | Lição em português sobre o que entra e o que sai da janela de contexto. |
| 4 | [anthropics/courses](https://github.com/anthropics/courses) | Anthropic | Curso | EN | Grátis | Cursos em notebooks, do prompt básico ao uso de ferramentas. |
| 5 | [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Anthropic | Artigo | EN | Grátis | Por que o contexto é um recurso finito e como gastá-lo bem. |

## 3. Embeddings e busca vetorial

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Construindo Aplicações de Busca](https://github.com/microsoft/generative-ai-for-beginners/tree/main/translations/pt-BR/08-building-search-applications) | Microsoft (IA Generativa para Iniciantes) | Curso | PT-BR | Grátis | Lição em português sobre busca semântica com embeddings. |
| 2 | [Embeddings: What they are and why they matter](https://simonwillison.net/2023/Oct/23/embeddings/) | Simon Willison | Artigo | EN | Grátis | Explicação prática com exemplos de busca e agrupamento. |
| 3 | [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/) | Jay Alammar | Guia | EN | Grátis | A origem da ideia de palavra como vetor, bem ilustrada. |
| 4 | [What is a Vector Database & How Does it Work? Use Cases + Examples](https://www.pinecone.io/learn/vector-database/) | Pinecone | Guia | EN | Grátis | Índices, similaridade e busca aproximada explicados por quem vende o banco. |
| 5 | [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) | Hugging Face | Ferramenta | EN | Grátis | Ranking público para escolher o modelo de embedding certo. |

## 4. RAG (geração aumentada por recuperação)

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Geração Aumentada por Recuperação (RAG) e Bancos de Dados Vetoriais](https://github.com/microsoft/generative-ai-for-beginners/tree/main/translations/pt-BR/15-rag-and-vector-databases) | Microsoft (IA Generativa para Iniciantes) | Curso | PT-BR | Grátis | Lição em português que liga embeddings, banco vetorial e RAG. |
| 2 | [Retrieval-Augmented Generation (RAG)](https://www.pinecone.io/learn/retrieval-augmented-generation/) | Pinecone | Guia | EN | Grátis | Visão completa do fluxo de RAG e de seus pontos de falha. |
| 3 | [Contextual retrieval in AI systems](https://www.anthropic.com/research/contextual-retrieval) | Anthropic | Artigo | EN | Grátis | Técnica com números medidos para reduzir falhas de recuperação. |
| 4 | [Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/) | Eugene Yan | Artigo | EN | Grátis | Padrões de produção, com RAG, evals e cache no mesmo mapa. |
| 5 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | Lewis et al. (Meta AI) | Artigo científico | EN | Grátis | O artigo que deu nome ao RAG. |

## 5. Agentes, ferramentas e MCP

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Agentes de IA para Iniciantes](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/pt-BR/README.md) | Microsoft | Curso | PT-BR | Grátis | Curso em português com lições de ferramentas, padrões de agente e MCP. |
| 2 | [Building effective AI agents](https://www.anthropic.com/research/building-effective-agents) | Anthropic | Artigo | EN | Grátis | O texto de referência sobre fluxos e agentes, com o mínimo de framework. |
| 3 | [Writing effective tools for AI agents](https://www.anthropic.com/research/writing-tools-for-agents) | Anthropic | Artigo | EN | Grátis | Como desenhar ferramentas que o modelo usa bem. |
| 4 | [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro) | Model Context Protocol | Documentação | EN | Grátis | Documentação oficial do protocolo, com guias de servidor e cliente. |
| 5 | [AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) | Hugging Face | Curso | EN | Grátis | Curso prático de agentes com exercícios e certificado. |

## 6. Programar com IA (Claude Code e similares)

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Visão geral do Claude Code](https://code.claude.com/docs/pt/overview) | Anthropic | Documentação | PT-BR | Grátis | Documentação oficial em português, do primeiro uso aos recursos avançados. |
| 2 | [Melhores práticas para Claude Code](https://code.claude.com/docs/pt/best-practices) | Anthropic | Documentação | PT-BR | Grátis | Como dar contexto, planejar e verificar o trabalho do agente. |
| 3 | [Here's how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) | Simon Willison | Artigo | EN | Grátis | Rotina realista de quem programa com LLM todo dia, sem exagero. |
| 4 | [Claude Code: A Highly Agentic Coding Assistant](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant) | DeepLearning.AI e Anthropic | Curso | EN | Grátis por tempo limitado | Curso curto com projetos reais feitos no Claude Code. |

## 7. Avaliação (evals) e confiabilidade

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Agentes de IA em Produção: Observabilidade e Avaliação](https://github.com/microsoft/ai-agents-for-beginners/tree/main/translations/pt-BR/10-ai-agents-production) | Microsoft (AI Agents for Beginners) | Curso | PT-BR | Grátis | Lição em português sobre medir e monitorar agentes em produção. |
| 2 | [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) | Hamel Husain | Artigo | EN | Grátis | O texto que popularizou evals como rotina de produto. |
| 3 | [Task-Specific LLM Evals that Do & Don't Work](https://eugeneyan.com/writing/evals/) | Eugene Yan | Artigo | EN | Grátis | Quais métricas valem para cada tarefa e quais enganam. |
| 4 | [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) | Anthropic | Artigo | EN | Grátis | Como a Anthropic avalia agentes que fazem várias etapas. |
| 5 | [AI Engineering: Building Applications with Foundation Models](https://huyenchip.com/books/) | Chip Huyen (O'Reilly, 2025) | Livro | EN | De R$ 105 a R$ 330 na Amazon BR | O melhor livro de engenharia de IA. Os capítulos de avaliação valem a compra. |

## 8. IA local (Whisper, TTS, Ollama, modelos abertos)

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Modelos open source (lição 16)](https://github.com/microsoft/generative-ai-for-beginners/tree/main/translations/pt-BR/16-open-source-models) | Microsoft (IA Generativa para Iniciantes) | Curso | PT-BR | Grátis | Lição em português sobre o que são modelos abertos e como escolher. |
| 2 | [Ollama documentation](https://docs.ollama.com/) | Ollama | Documentação | EN | Grátis | Instalação, API e modelos para rodar LLMs na própria máquina. |
| 3 | [openai/whisper](https://github.com/openai/whisper) | OpenAI | Ferramenta | EN | Grátis | Repositório oficial do Whisper, com tamanhos de modelo e uso em Python. |
| 4 | [Hugging Face Audio course](https://huggingface.co/learn/audio-course/chapter0/introduction) | Hugging Face | Curso | EN | Grátis | Transcrição e síntese de voz com modelos abertos, do zero. |
| 5 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | Qwen (Alibaba Cloud) | Ferramenta | EN | Grátis | Modelo aberto de síntese de voz para rodar localmente. |

## 9. Custo, segurança e prompt injection

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [OWASP Top 10 para Aplicações de LLM e IA Generativa (2025)](https://genai.owasp.org/resource/owasp-top-10-para-aplicacoes-de-llm-e-ia-generativa-2025/) | OWASP | Guia | PT-BR | Grátis | A lista de riscos de referência do setor, em português. |
| 2 | [Protegendo suas Aplicações de IA Generativa](https://github.com/microsoft/generative-ai-for-beginners/tree/main/translations/pt-BR/13-securing-ai-applications) | Microsoft (IA Generativa para Iniciantes) | Curso | PT-BR | Grátis | Lição em português sobre ameaças e defesas em apps de IA. |
| 3 | [Mitigar jailbreaks e injeções de prompt](https://platform.claude.com/docs/pt-BR/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) | Anthropic | Documentação | PT-BR | Grátis | Defesas práticas contra jailbreak e prompt injection. |
| 4 | [The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) | Simon Willison | Artigo | EN | Grátis | A regra mais útil para saber quando um agente pode vazar dados. |
| 5 | [Cache de prompt](https://platform.claude.com/docs/pt-BR/build-with-claude/prompt-caching) | Anthropic | Documentação | PT-BR | Grátis | Como cortar custo e latência reaproveitando o mesmo contexto. |
