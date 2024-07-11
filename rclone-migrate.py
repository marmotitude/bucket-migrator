import subprocess

profile1 = 'profile1'  # Nome do perfil de origem
profile2 = 'profile2'  # Nome do perfil de destino
prefix = '-prefix'  # Prefixo para os buckets de destino
bucket_list = ['bucket-1', 'bucket-2']  # Lista de buckets a serem migrados
# Configuração para acelerar o upload
transfers = 16 # Define quantidade de transferências simultaneas

# Loop through each bucket and perform the migration tasks
for bucket in bucket_list:
    # Create the destination directory
    print('Bucket', bucket + prefix, 'criado no remoto', profile2)
    mkdir_result = subprocess.run(['rclone', 'mkdir', f'{profile2}:{bucket}{prefix}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Check if mkdir was successful
    if mkdir_result.returncode == 0:
        print('Bucket', bucket, 'sendo migrado com o nome', bucket + prefix, 'para o remoto', profile2, '...')
        sync_result = subprocess.run(['rclone', 'sync', f'{profile1}:{bucket}', f'{profile2}:{bucket}{prefix}', '--transfers', f'{transfers}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if sync was successful
        if sync_result.returncode == 0:
            print(f"Bucket: {bucket} migrado para {profile2} com sucesso.")
        else:
            print(f"Erro ao sincronizar bucket {bucket}: {sync_result.stderr}")
    else:
        print(f"Erro ao criar diretório para bucket {bucket}: {mkdir_result.stderr}")

print("Todos os buckets foram processados.")
