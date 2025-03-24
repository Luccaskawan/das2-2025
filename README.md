# Aula – 27/02/25


## Projeto de Sistemas e Trade-offs
- Sempre que projetamos um sistema, fazemos escolhas. Muitas vezes optamos por tecnologias que conhecemos, mas elas nem sempre são as melhores para o problema.




## Consistência e Durabilidade
- Nem todos os sistemas precisam ser totalmente consistentes.
- Durabilidade garante que os dados sejam gravados permanentemente, mas o uso de cache pode reduzir essa garantia em troca de desempenho.




## Normalização e Terceira Forma Normal
- Aplicar a terceira forma normal ajuda a reduzir redundâncias e eliminar dados repetidos, tornando o banco de dados mais eficiente.




## Escalabilidade
- O site da Univille usa servidores potentes, mas enfrenta gargalos com PHP.
- A solução é a escalabilidade elástica: adicionar mais máquinas em períodos de pico (ex.: semana de notas) e reduzir quando a demanda cai.




## Automação e Infraestrutura como Código
- Implementar detecção automática de falhas e mecanismos de auto-recuperação (self-healing).
- Substituir configurações manuais por scripts automatizados.
- Tratar servidores e recursos como descartáveis, permitindo fácil substituição e replicação.


# Aula – 06/03/25


## Trade-off  
A Unville optou por comprar um servidor próprio, o que pode não ter sido a melhor decisão. Uma alternativa mais eficiente seria utilizar a nuvem, pois permite escalar a capacidade computacional conforme a demanda, especialmente durante lançamentos de novas máquinas, otimizando custos e recursos.  


## Infraestrutura como Código (IaC)  
Gerenciar infraestrutura manualmente torna o ambiente frágil e dependente de quem realizou a configuração inicial. Com IaC, os recursos são tratados como descartáveis, permitindo recriação rápida e segura da base sempre que necessário, garantindo maior confiabilidade e facilidade de manutenção.  


## Baixo Acoplamento  
Um exemplo de arquitetura com baixo acoplamento é o uso de múltiplas réplicas de banco de dados distribuídas por um load balancer. Esse modelo permite substituir máquinas sem afetar a operação do sistema, garantindo maior disponibilidade e resiliência.  


## Escolha do Banco de Dados Correto  
Ao projetar um sistema, é essencial escolher entre bancos de dados relacionais e NoSQL.  


- **Bancos de Dados Relacionais:**  
  - Utilizados em aproximadamente **90% das aplicações**.  
  - Modelo tradicional, baseado em tabelas e relacionamentos.  
  - Limitação na **escalabilidade horizontal** (número finito de réplicas).  


- **Bancos de Dados NoSQL:**  
  - Nome correto: **"Not Only SQL"** (não se limita a um único modelo de dados).  
  - Permitem **escalabilidade horizontal praticamente ilimitada**.  
  - São indicados para aplicações que exigem alto volume de dados e performance.  


## Evitar Pontos Únicos de Falha  
A redundância é essencial para garantir a disponibilidade do sistema. Arquiteturas resilientes evitam pontos únicos de falha, garantindo que a aplicação continue operando mesmo em caso de falhas em componentes individuais.  


## Otimização de Custos  
Serviços gerenciados na nuvem ajudam a reduzir custos, pois evitam a necessidade de manter infraestrutura própria e reduzem despesas operacionais.  


> *"Jeff Bezos (AWS) não quer que você gaste demais com máquinas, porque se ficar insustentável para você, você sairá da AWS e ambos perdem. A melhor estratégia é otimizar seus recursos para um uso eficiente e sustentável."*  


🔹 Utilize **serviços gerenciados** para reduzir custos e aumentar a eficiência operacional.  

# Aula 10/03/25 – Infraestrutura e Segurança na AWS  

## 📌 Infraestrutura da AWS  

- **Região da AWS**: Área geográfica que contém várias infraestruturas de computação.  
  - No Brasil, a região disponível é **southamerica-1** (São Paulo).  

- **AZ (Zona de Disponibilidade)**:  
  - São grupos de um ou mais **data centers** dentro de uma região.  
  - Em **São Paulo**, existem **três AZs**.  

- **Local Zone**:  
  - Funciona de forma semelhante a uma AZ, mas tem menor capacidade.  
  - Na América do Sul, há uma em **Buenos Aires, Argentina**.  

- **Diferença entre AZ e Local Zone**:  
  - Ambas oferecem serviços semelhantes, mas a **Local Zone é menor**.  

- **Edge Location**:  
  - São **pontos de presença (PoP)** que melhoram a entrega de conteúdos e serviços.  
  - Existem **mais de 700** espalhados pelo mundo.  

---

## 🔒 Segurança de Acesso  

### 🔹 **Modelo de Responsabilidade Compartilhada da AWS**  
- A **AWS** é responsável pela **segurança da nuvem** (infraestrutura, servidores, rede).  
- O **cliente** é responsável pela **segurança dentro da nuvem** (configurações, permissões, dados).  

### 🔹 **Tipos de Serviço e Segurança**  
- **IaaS (Infraestrutura como Serviço)** → Exemplo: **EC2 (servidores virtuais)**.  
- **SaaS (Software como Serviço)** → Exemplo: **S3 (armazenamento de objetos)** com criptografia **SSE-S3**.  

### 🔹 **Proteção contra Ataques**  
- Ataques como **vírus trojan** podem sequestrar dados.  
- Métodos de criptografia ajudam a proteger informações:  
  - **SSE-C**  
  - **SSE-S3**  
  - **SSE-KMS**  

### 🔹 **Gerenciamento de Permissões**  
- Os usuários devem receber **apenas as permissões necessárias** para suas funções.  
- Isso evita acessos desnecessários e reduz riscos de segurança.  

---

# 📚 Aula 17/03 – Policies, Permissões e Armazenamento na AWS  

## 🔑 Diferentes Policies e Permissões  

### ✅ **Policy de Recurso**  
- Define permissões diretamente em um recurso específico.  
- **Exemplo**: No **S3**, é possível criar uma policy no **bucket**, permitindo ou negando acessos.  
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
- **EBS (Elastic Block Store)** → Armazenamento de **blocos** para instâncias EC2.  
- **EFS (Elastic File System)** → Armazenamento **de arquivos**, escalável e compartilhado.  
- **FSx** → Armazenamento otimizado para **Windows e Lustre**.  
- **S3 (Simple Storage Service)** → Armazenamento de **objetos**.  

---






