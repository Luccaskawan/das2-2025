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



