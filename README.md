# 📚 Aula – 27/02/25  

## ⚖ Projeto de Sistemas e Trade-offs  
- Sempre que projetamos um sistema, fazemos escolhas.  
- Muitas vezes, optamos por tecnologias que conhecemos, mas elas nem sempre são as melhores para o problema.  

---

## 🔄 Consistência e Durabilidade  
- Nem todos os sistemas precisam ser **totalmente consistentes**.  
- **Durabilidade** garante que os dados sejam gravados permanentemente, mas o uso de **cache** pode reduzir essa garantia em troca de desempenho.  

---

## 📊 Normalização e Terceira Forma Normal  
- Aplicar a **Terceira Forma Normal (3FN)** ajuda a reduzir **redundâncias** e eliminar dados repetidos.  
- Isso torna o banco de dados mais eficiente e fácil de gerenciar.  

---

## 📈 Escalabilidade  
- O site da **Univille** usa **servidores potentes**, mas enfrenta gargalos com **PHP**.  
- A solução é a **escalabilidade elástica**:  
  - Adicionar mais máquinas em períodos de pico (*ex.: semana de notas*).  
  - Reduzir quando a demanda cai, economizando recursos.  

---

## 🤖 Automação e Infraestrutura como Código  
- Implementar **detecção automática de falhas** e mecanismos de **auto-recuperação (self-healing)**.  
- Substituir **configurações manuais** por **scripts automatizados**.  
- Tratar **servidores e recursos como descartáveis**, permitindo fácil substituição e replicação.  

---

# 📚 Aula – 06/03/25  

## ⚖ Trade-off  
- A **Univille** optou por comprar um **servidor próprio**, mas pode não ter sido a melhor decisão.  
- Uma alternativa mais eficiente seria a **nuvem**, que permite:  
  - **Escalar a capacidade computacional** conforme a demanda.  
  - **Otimizar custos e recursos** sem precisar investir em hardware próprio.  

---

## 🏗 Infraestrutura como Código (IaC)  
- Gerenciar infraestrutura **manualmente** torna o ambiente **frágil** e dependente de quem fez a configuração inicial.  
- Com **IaC**, os recursos são **descartáveis**, permitindo:  
  - **Recriação rápida e segura** do ambiente.  
  - **Maior confiabilidade e facilidade de manutenção**.  

---

## 🔗 Baixo Acoplamento  
- Um **exemplo de arquitetura desacoplada** é o uso de **múltiplas réplicas** de banco de dados distribuídas por um **load balancer**.  
- Vantagens:  
  - **Substituir máquinas sem afetar o sistema**.  
  - **Maior disponibilidade e resiliência**.  

---

## 🗄 Escolha do Banco de Dados Correto  

### 🏛 **Bancos de Dados Relacionais**  
- Utilizados em aproximadamente **90% das aplicações**.  
- Modelo tradicional, baseado em **tabelas e relacionamentos**.  
- Limitação na **escalabilidade horizontal** (*número finito de réplicas*).  

### 📦 **Bancos de Dados NoSQL**  
- Nome correto: **"Not Only SQL"** (*não se limita a um único modelo de dados*).  
- Permitem **escalabilidade horizontal praticamente ilimitada**.  
- Indicados para **alto volume de dados e alta performance**.  

---

## 🚨 Evitar Pontos Únicos de Falha  
- A **redundância** é essencial para garantir a **disponibilidade do sistema**.  
- Arquiteturas resilientes evitam **pontos únicos de falha**, garantindo que a aplicação continue operando mesmo se um componente falhar.  

---

## 💰 Otimização de Custos  
- **Serviços gerenciados** na nuvem ajudam a reduzir custos, pois:  
  - **Evitam manter infraestrutura própria**.  
  - **Reduzem despesas operacionais**.  

> *"Jeff Bezos (AWS) não quer que você gaste demais com máquinas, porque se ficar insustentável para você, você sairá da AWS e ambos perdem. A melhor estratégia é otimizar seus recursos para um uso eficiente e sustentável."*  

✅ **Utilize serviços gerenciados** para reduzir custos e aumentar a eficiência operacional.  

---

# 📚 Aula – 10/03/25 – Infraestrutura e Segurança na AWS  

## 📌 Infraestrutura da AWS  

- **Região da AWS**: Área geográfica que contém várias infraestruturas de computação.  
  - No Brasil, a região disponível é **southamerica-1** (*São Paulo*).  

- **AZ (Zona de Disponibilidade)**:  
  - São grupos de um ou mais **data centers** dentro de uma região.  
  - Em **São Paulo**, existem **três AZs**.  

- **Local Zone**:  
  - Funciona como uma **AZ menor**.  
  - Na América do Sul, há uma em **Buenos Aires, Argentina**.  

- **Edge Location**:  
  - **Pontos de presença (PoP)** para melhorar entrega de conteúdos.  
  - Existem **+700** espalhados pelo mundo.  

---

## 🔒 Segurança de Acesso  

### 🔹 **Modelo de Responsabilidade Compartilhada da AWS**  
- A **AWS** cuida da **segurança da nuvem** (infraestrutura, servidores, rede).  
- O **cliente** cuida da **segurança dentro da nuvem** (configurações, permissões, dados).  

### 🔹 **Tipos de Serviço e Segurança**  
- **IaaS (Infraestrutura como Serviço)** → Exemplo: **EC2 (servidores virtuais)**.  
- **SaaS (Software como Serviço)** → Exemplo: **S3 (armazenamento de objetos)** com criptografia **SSE-S3**.  

### 🔹 **Proteção contra Ataques**  
- **Vírus trojan** podem sequestrar dados.  
- Métodos de criptografia para proteção:  
  - **SSE-C**  
  - **SSE-S3**  
  - **SSE-KMS**  

### 🔹 **Gerenciamento de Permissões**  
- Os usuários devem receber **apenas as permissões necessárias**.  
- Evita acessos desnecessários e reduz riscos de segurança.  

---

# 📚 Aula – 17/03/25 – Policies, Permissões e Armazenamento na AWS  

## 🔑 Diferentes Policies e Permissões  

### ✅ **Policy de Recurso**  
- Define permissões diretamente em um recurso.  
- **Exemplo**: No **S3**, é possível criar uma **policy no bucket**.  
- Permite um controle **mais granular** das permissões.  

### ⚖ **Diferença entre Policy de Identidade vs. Policy de Recurso**  
| Tipo de Policy       | Aplicação                                      | Característica |
|----------------------|-----------------------------------------------|---------------|
| **Policy de Identidade** | Aplicada a usuários, grupos ou roles do IAM. | Contém `"Principal": {}`. |
| **Policy de Recurso**  | Aplicada diretamente ao recurso (exemplo: S3). | **Não** contém `"Principal": {}`. |

### 🔄 **Ordem de Avaliação das Permissões na AWS**  
1. **A AWS reúne todas as policies** associadas ao usuário.  
2. **Primeiro, verifica os "Deny"** explícitos.  
3. **Depois, verifica os "Allow"**.  
4. **Por padrão, tudo que não está citado é negado (Implicit Deny)**.  

---

## 💾 Armazenamento em Blocos  

### 📂 **Principais tipos de storage na AWS**  
- **EBS (Elastic Block Store)** → Armazenamento de **blocos** para EC2.  
- **EFS (Elastic File System)** → Armazenamento **de arquivos**, escalável e compartilhado.  
- **FSx** → Armazenamento otimizado para **Windows e Lustre**.  
- **S3 (Simple Storage Service)** → Armazenamento de **objetos**.  

---

# 📚 Aula – 24/03/25 – Armazenamento e Segurança no S3

## 💾 Configuração de Armazenamento no S3  
- É essencial **definir regras de ciclo de vida** desde o início.  
- Caso contrário, **os dados podem se acumular** e gerar **altos custos**.  
- Exemplo de regra útil:  
  - **Mover automaticamente** arquivos para classes de armazenamento mais baratas.  
  - **Excluir** objetos antigos após determinado período.

> ⚠️ *“Defina uma regra cedo, senão vai dar merda.”*  

---

## 🕓 Versionamento no S3  
- Por padrão, o **versionamento não vem habilitado**.  
- Uma vez **ativado**, **não é possível desativar** (apenas suspender).  
- Ao **alterar ou excluir** um objeto, o S3 **cria uma nova versão** em vez de sobrescrever.  
- Isso impacta diretamente no **custo**, pois **todas as versões são armazenadas**.

---

## 🔐 Configurações Padrões de Segurança no S3  

### 🛡 Server-side Encryption  
- A **AWS realiza a criptografia** dos dados **automaticamente**, no lado do servidor.  
- Tipos comuns:  
  - **SSE-S3**  
  - **SSE-KMS**  
  - **SSE-C**

### 🔑 Client-side Encryption  
- A **criptografia é feita pelo cliente**, antes do envio para o S3.  
- O cliente também é responsável por **gerenciar as chaves** de criptografia.  

---

# 📚 Aula – 03/04/25 – Amazon EC2

## 🖥️ Amazon EC2  
- Serviço de computação escalável baseado em **máquinas virtuais**.  
- É possível utilizar EC2 para **rodar funções Lambda**, embora essa não seja a prática mais comum (Lambda é serverless, EC2 não).  
- Flexível, com suporte a múltiplos sistemas operacionais, tipos de instância e configurações de rede.

---

## 📦 Armazenamento Efêmero – Instance Store  
- O **armazenamento efêmero** é chamado de **Instance Store**.  
- Armazenamento **local**, anexado fisicamente ao host da instância.  
- ⚠️ **Dados são perdidos** se a instância for interrompida, parada ou terminada.  
- Ideal para dados temporários, como:  
  - **Cache**  
  - **Dados de sessão**  
  - **Arquivos de processamento temporário**

---

# 📚 Aula – 07/04/25 – Armazenamento e Banco de Dados na AWS

## 📂 Amazon FSx  
- Serviço de armazenamento gerenciado que oferece sistemas de arquivos otimizados.  
- O **Amazon FSx for Windows File Server** trabalha com **NTFS**, o mesmo sistema de arquivos usado em servidores Windows.  
- Ideal para **aplicações que precisam de compatibilidade com Windows**, como:  
  - Active Directory  
  - Permissões NTFS  
  - Aplicações corporativas legadas

---

## 💾 Amazon EBS (Elastic Block Store)  
- Oferece armazenamento em **blocos persistente** para instâncias EC2.  
- Diferente do **Instance Store**, os dados do EBS **persistem mesmo após a instância ser desligada**.  
- Ideal para:  
  - **Sistemas operacionais**  
  - **Bancos de dados**  
  - **Aplicações que exigem alta durabilidade dos dados**

---

## 🛢️ Reserved Instances no RDS  
- O **Amazon RDS** permite reservar instâncias para economizar custos a longo prazo.  
- As **Reserved Instances (RI)** oferecem **descontos significativos** em comparação com instâncias sob demanda.  
- Períodos comuns: **1 ano ou 3 anos**.  
- Ideal para aplicações **com carga previsível e uso contínuo**.

---

# 📚 Aula – 10/04/25 – Considerações sobre Bancos de Dados

## 📈 Database Considerations  
- Ao escolher um banco de dados, é importante considerar:  
  - **Escalabilidade**: Capacidade de crescer com a demanda.  
  - **Requisitos de espaço**: Volume de dados esperado.  
  - **Características dos dados**: Estrutura fixa ou variável.  
  - **Durabilidade**: Garantia de que os dados serão preservados com segurança.

---

## 🏛️ Banco de Dados Relacional vs Não Relacional  

### 🗂 Relacional  
- Estrutura baseada em **tabelas com esquemas fixos**.  
- É necessário **definir os campos e tipos de dados** com antecedência.  
- Ideal para dados **estruturados e com relações claras**.

### 📦 Não Relacional  
- **Não exige campos definidos**, podendo inclusive conter **valores vazios**

---

# 📚 Aula – 08/05/25 – Redes, Segurança e VPC na AWS

## 🌐 VPC e Subnets Privadas  
- A **VPC (Virtual Private Cloud)** permite criar uma rede isolada na AWS.  
- Dentro da VPC, é possível configurar **subnets públicas e privadas**.  
- **Subnets privadas** **não têm acesso direto à internet**, aumentando a segurança.  

---

## 🌐 Conectando Subnet Privada à Internet  
- Para permitir que uma subnet privada acesse a internet:  
  - Usar um **NAT Gateway** em uma subnet pública.  
  - Em ambientes de alta disponibilidade, utilizar **duplo NAT Gateway** (um por zona de disponibilidade).  
- O tráfego sai da subnet privada, passa pelo NAT e então vai à internet.

---

## 🔐 Security Groups e Network ACL  
- **Security Groups**:  
  - Atuando como **firewall virtual** para instâncias.  
  - Funcionam com **regras de entrada e saída baseadas em permissões por instância**.  
  - **Stateful**: se o tráfego de entrada é permitido, o de saída correspondente também é.

- **Network ACL (Access Control List)**:  
  - Aplicada ao **nível da subnet**.  
  - Controla **tráfego de entrada e saída** com regras **explícitas** de **allow/deny**.  
  - **Stateless**: cada direção precisa de regras específicas.

---

## 🔥 AWS Network Firewall  
- Serviço gerenciado de firewall para proteção de redes dentro da VPC.  
- Oferece:  
  - **Filtragem de tráfego baseada em regras personalizadas**.  
  - **Inspeção profunda de pacotes (DPI)**.  
  - **Controle de aplicações e domínios acessados**.  
- Ideal para redes que exigem **monitoramento e controle avançado de segurança**.

---
 
# 📚 Aula – 16/06/25 – Load Balancer e DNS na AWS

## ⚖️ Load Balancer e Suas Variações  
- O **Load Balancer** distribui o tráfego entre múltiplos destinos (instâncias, IPs, containers).  
- Tipos principais na AWS:  

### 🌐 Application Load Balancer (ALB)  
- Atua na **camada 7 (HTTP/HTTPS)**.  
- Permite **roteamento baseado em URL, host ou headers**.  
- Ideal para **aplicações web** e microsserviços.

### 🌐 Network Load Balancer (NLB)  
- Atua na **camada 4 (TCP/UDP)**.  
- Suporta **alta performance e baixa latência**.  
- Indicado para sistemas que precisam de **milhões de conexões por segundo**.

### 🌐 Gateway Load Balancer (GLB)  
- Usado para integrar **appliances virtuais** de terceiros.  
- Ideal para **firewalls, sistemas de inspeção ou segurança avançada**.  
- Trabalha com tráfego encapsulado (**GWLBe**).

### 🌐 Classic Load Balancer (CLB)  
- Suporta **camada 4 e 7**, mas é **legado**.  
- Substituído pelo **ALB e NLB** em novos projetos.  
- Ainda usado em **ambientes antigos**.

---

## 🧩 Componentes do Load Balancer  
- **Listeners**: portas que recebem o tráfego de entrada (ex: 80, 443).  
- **Target Groups**: conjunto de destinos que receberão o tráfego.  
- **Health Checks**: verificações periódicas para garantir que os destinos estão ativos.  

---

## 🌍 DNS na AWS  
- O **DNS (Domain Name System)** traduz nomes de domínio em endereços IP.  
- A AWS oferece o **Route 53**, serviço gerenciado de DNS com:  
  - **Alta disponibilidade**  
  - **Balanceamento geográfico**  
  - **Failover automático**  
- O DNS é responsável por redirecionar os acessos para o **load balancer**.

---

## 🔗 Redução de Acoplamento em Sistemas

- Reduzir o **acoplamento** facilita a **manutenção**, a **escalabilidade** e a **resiliência** do sistema.  
- Um sistema bem desacoplado permite **alterações em módulos isolados** sem afetar o restante da aplicação.

### 🛠 Estratégias para Reduzir Acoplamento

- **Load Balancer**  
  - Distribui o tráfego entre instâncias.  
  - Ajuda na escalabilidade, mas não separa a lógica entre componentes.

- **Módulos (quase microserviços)**  
  - Partes do sistema com responsabilidades isoladas.  
  - Reduzem dependências diretas, mas ainda compartilham recursos.

- **Microserviços**  
  - Arquitetura onde cada serviço é totalmente independente.  
  - Cada um possui sua lógica, banco de dados e ciclo de vida próprios.

- **📣 Publish/Subscribe Messaging**  
  - Comunicação via troca de mensagens assíncronas.  
  - Um componente “publica” uma mensagem; os demais “assinam” se desejarem responder.  
  - Permite **comunicação desacoplada**, ideal para arquiteturas distribuídas.

> ✅ **Combinar microserviços com Publish/Subscribe** é uma das formas mais eficientes de reduzir acoplamento em sistemas modernos.
