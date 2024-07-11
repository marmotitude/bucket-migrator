# Bucket Migration Script

Este script Python é utilizado para migrar buckets entre dois perfis usando `rclone`. Ele cria os diretórios de destino e sincroniza os conteúdos dos buckets de origem para os buckets de destino. O script é útil para automatizar a migração de múltiplos buckets de forma eficiente.

## Pré-requisitos

1. **rclone**: Certifique-se de que o `rclone` esteja instalado e configurado em seu sistema. Você pode seguir as instruções de instalação no [site oficial do rclone](https://rclone.org/install/).

2. **Perfis Configurados**: Configure os perfis `rclone` para os dois ambientes entre os quais deseja migrar os buckets. As configurações dos perfis podem ser encontradas no arquivo de configuração do `rclone` (normalmente localizado em `~/.config/rclone/rclone.conf`).

## Variáveis do Script

Antes de executar o script, você precisará ajustar as seguintes variáveis:

1. **`profile1`**: Nome do perfil `rclone` de origem (onde os buckets atuais estão localizados).
2. **`profile2`**: Nome do perfil `rclone` de destino (onde os buckets serão migrados).
3. **`prefix`**: Prefixo a ser adicionado ao nome do bucket de destino. Como os buckets são unicos globalmente, o bucket destino precisa ter um nome diferente da origem.
4. **`bucket_list`**: Lista dos nomes dos buckets a serem migrados.
5. **`transfers`**: Define quantidade de transferências simultaneas.


## Como Usar
Edite as Variáveis: Altere as variáveis profile1, profile2, prefix e bucket_list no início do script para corresponder aos seus perfis e buckets específicos.

Execute o Script: Depois de fazer as alterações necessárias, execute o script com Python:

```sh
python rclone-migrate.py
```


## Informações complementares

[Melhores praticas rclone](https://docs.magalu.cloud/docs/object-storage/tutorials/rclone-best-practices)
