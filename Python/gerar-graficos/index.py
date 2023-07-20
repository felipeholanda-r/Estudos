import matplotlib.pyplot as plt

def criar_grafico_gauge(valor, limite, titulo):
    # Configurações do gráfico de gauge
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Desenhar o arco do gauge
    ax.add_patch(plt.Circle((0, 0), radius=0.75, facecolor='white', edgecolor='gray', linewidth=3))
    ax.add_patch(plt.Circle((0, 0), radius=0.65, facecolor='lightgray', edgecolor='gray', linewidth=2))
    ax.add_patch(plt.Circle((0, 0), radius=0.55, facecolor='white', edgecolor='gray', linewidth=2))

    # Calcular o ângulo do valor atual
    angulo = (valor / limite) * 180

    # Desenhar a seta indicadora
    ax.add_patch(plt.Arrow(0, 0, 0.4, 0, width=0.3, color='gray'))
    ax.add_patch(plt.Arrow(0, 0, 0.35, 0, width=0.4, color='black'))

    # Adicionar o texto do valor
    ax.text(0, -0.2, f'{valor}', ha='center', va='center', fontsize=20)

    # Personalizar o gráfico
    ax.set_title(titulo, fontsize=14)
    ax.axis('off')

    # Salvar o gráfico em um arquivo PDF
    plt.savefig('gauge.pdf', format='pdf')

    # Exibir uma mensagem de confirmação
    print("Gráfico de gauge salvo como 'gauge.pdf'")

# Exemplo de uso
valor_atual = 75
limite = 100
titulo = 'Gauge'

criar_grafico_gauge(valor_atual, limite, titulo)
