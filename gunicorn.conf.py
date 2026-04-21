# gunicorn.conf.py
# Configuração do servidor de produção para o Render
# O Render usa este ficheiro automaticamente ao arrancar

import eventlet
eventlet.monkey_patch()  # necessário para o SocketIO funcionar em produção

# Número de processos (1 é obrigatório com SocketIO + eventlet)
workers = 1

# Tipo de worker que suporta WebSockets (tempo real)
worker_class = "eventlet"

# Porta que o Render atribui automaticamente via variável de ambiente
bind = "0.0.0.0:10000"

# Logs visíveis no painel do Render
loglevel = "info"
accesslog = "-"
errorlog  = "-"
