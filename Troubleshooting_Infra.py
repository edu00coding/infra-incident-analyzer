import pandas as pd

inventario = [

   {"id_host": "SRV-01", "hostname": "WebServer-Prod-SP", "setor": "E-commerce"},
    {"id_host": "SRV-02", "hostname": "Database-Core-ST", "setor": "Financeiro"},
    {"id_host": "SRV-03", "hostname": "Auth-Service-Global", "setor": "Segurança"},
    {"id_host": "SRV-04", "hostname": "Backup-Storage-01", "setor": "Infra"},
    {"id_host": "SRV-05", "hostname": "Proxy-Nginx-SP", "setor": "E-commerce"},
    {"id_host": "SRV-06", "hostname": "Redis-Cache-Cluster", "setor": "E-commerce"},
    {"id_host": "SRV-07", "hostname": "AD-Controller-Primary", "setor": "Infra"},
    {"id_host": "SRV-08", "hostname": "Zabbix-Monitor-01", "setor": "Monitoração"},
    {"id_host": "SRV-09", "hostname": "Dev-Docker-Worker", "setor": "Desenvolvimento"},
    {"id_host": "SRV-10", "hostname": "ERP-Backend-App", "setor": "Financeiro"}

]

logs_erro = [

    {"host": "SRV-01", "evento": {"erro": "Timeout", "critico": True, "codigo": 504}},
    {"host": "SRV-02", "evento": {"erro": "Disk Full", "critico": True, "codigo": 101}},
    {"host": "SRV-05", "evento": {"erro": "SSH Brute Force", "critico": True, "codigo": 403}},
    {"host": "SRV-01", "evento": {"erro": "404 Not Found", "critico": False, "codigo": 404}},
    {"host": "SRV-09", "evento": {"erro": "High Latency", "critico": False, "codigo": 200}},
    {"host": "SRV-10", "evento": {"erro": "Memory Leak", "critico": True, "codigo": 500}},
    {"host": "SRV-11", "evento": {"erro": "Unknown Host", "critico": True, "codigo": 999}}, # Externo
    {"host": "SRV-03", "evento": {"erro": "Expired Certificate", "critico": True, "codigo": 443}}
]


df_inventario = pd.DataFrame(inventario)

log_normalizado = pd.json_normalize(logs_erro)

relatorio_final = pd.merge(df_inventario, log_normalizado,left_on='id_host', right_on= 'host' , how='left')

relatorio_final['evento.erro'] = relatorio_final['evento.erro'].fillna('Sem Erros')
relatorio_final['evento_critico'] = relatorio_final['evento.critico'].fillna(False)
incidentes_graves = relatorio_final[relatorio_final['evento.critico'] == True ]


incidentes_graves.to_csv('relatorio.csv', index= False)

print("\n--- RELATÓRIO DE INFRAESTRUTURA GERADO ---\n")
print(relatorio_final[['id_host', 'hostname', 'evento.erro', 'evento.critico']])
print(f"Total de incidentes ciriticos encontrados: {len(incidentes_graves)}")