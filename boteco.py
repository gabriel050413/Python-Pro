import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

perguntas = [
    {
        "pergunta": "A COP É UMA REUNIÃO BRASILEIRA QUE REÚNE OS ESTADOS BRASILEIROS PARA DISCUTIREM QUESTÕES AMBIENTAIS.",
        "resposta": False,
        "explicacao": "A COP É, NA VERDADE, UMA REUNIÃO INTERNACIONAL ONDE MAIS DE 100 PAÍSES DISCUTEM QUESTOES AMBIENTAIS EM PAÍSES SEDES VOTADOS."
    },
    {
        "pergunta": "É CORRETO DIZER QUE A SITUAÇÃO MUNDIAL ATUALMENTE PROCURA MELHORIAS SOB A POLUIÇÃO FEITA PELOS HUMANOS NAS ÉPOCAS DE REVOLUÇÃO INDUSTRIAL, QUE CONTRIBUIRAM PARA O AUMENTO DA POLUIÇÃO, DEVIDO A QUEIMA DE CARVÃO E PETROLE, PRINCIPAIS FONTES DE ENERGIA DA EPOCA.",
        "resposta": True,
        "explicacao": "ESTÁ CORRETO A AFIRMAÇÃO. PAÍSES NO MUNDO INTEIRO BUSCAM USAR FONTES LIMPAS E RENOVAVEIS PARA RECONSTRUIR O MUNDO."
    },
    {
        "pergunta": "PAÍSES EUROPEUS SÃO IDEPENDENETES DE BIOMAS E ECOSSISTEMAS AMERICANOS, VISTO QUE SUA CONDIÇÃO ECOLOGICA ESTÁ SEM COMPLICAÇOES",
        "resposta": False,
        "explicacao": "PA[ISES EUROPEUS NA VERDADE PERCISAM DA FLORESTA AMAZONICA, POR EXEMPLO, PARA CONTINUAREM RESISTINDO A QUESTOES DE SOBREVIVENCIA AMBIENTAL, POIS A FLORESTA AMAZONICA É O PULMÃO DO MUNDO]"
    },
    {
        "pergunta": "O USO DE FONTES NÃO RENOVAVEIS SIGNIFICA QUE A MESMA PODE DESTRUIR O MEIO AMBIENTE",
        "resposta": False,
        "explicacao": "Renovavel não é a mesma coisa de fonte limpa, pois uma fonte não renovavel significa que a fonte se renova mais lento do que a ultilizamos, fazendo a mesma se egotar rapido."
    },
]


def mensagem_final(pontos, total):
    if pontos == total:
        return "voce acertou tudo!"
    elif pontos >= total / 2:
        return "parabens"
    else:
        return "vai estudar"


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.command()
async def startquiz(ctx):
    pontos = 0

    for item in perguntas:
        msg = await ctx.send(item["pergunta"])
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")

        def verificar(payload):
            print(f"Reação recebida: {payload.emoji} de {payload.user_id}")
            return (
                payload.user_id == ctx.author.id
                and payload.message_id == msg.id
                and str(payload.emoji) in ["✅", "❌"]
            )

        try:
            payload = await bot.wait_for("raw_reaction_add", timeout=30, check=verificar)
        except asyncio.TimeoutError:
            await ctx.send("⏰ Tempo esgotado! Quiz encerrado.")
            return

        resposta_usuario = str(payload.emoji) == "✅"

        if resposta_usuario == item["resposta"]:
            pontos += 1
            await ctx.send(f"✅ Acertou! {item['explicacao']}")
        else:
            await ctx.send(f"❌ Errou! {item['explicacao']}")

    total = len(perguntas)
    await ctx.send(f"🏁 Fim do quiz! Você acertou {pontos} de {total} perguntas.")
    
bot.run("MTU1NDYyMjgyNDMzMTYxNjI1Ng.GYYbxA.dBHk9_B7h3y_d6K7T5WL0AUTFt-Eg-NXQfPRVg")
