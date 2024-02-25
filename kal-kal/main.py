import discord
from discord.ext import commands

# Створення бота
bot = commands.Bot(command_prefix='/')

# Обробник події запуску бота
@bot.event
async def on_ready():
    print(f'Бот підключено до Discord: {bot.user.name}')

@bot.command(name='hello')
async def hello(ctx):
    # Створення вбудованого повідомлення з текстом
    embed = discord.Embed(
        title='📜❘-правила',
        description=f"Правила сервера\n1. Звернення в особисті повідомлення - заборонено.\n2.Публікувати NSFW контент - заборонено.\n3. Спам та флуд - заборонено.\n4. Розсилка та реклама - заборонено.\n5. Використовуйте кожен канал суто по призначенню.\n\n Незнання правил не позбавляє від відповідальності",
        color=discord.Color.purple()
    )
    
    # Додавання зображення до вбудованого повідомлення
    embed.set_image(url="")
    
    # Відправлення вбудованого повідомлення разом з зображенням
    await ctx.send(embed=embed)
    
@bot.event
async def on_message(message):
    # Перевірка, чи повідомлення не від бота
    if message.author == bot.user:
        return

    # Видаляємо слово "хуйло" з повідомлення та надсилаємо змінене повідомлення
    cleaned_message = message.content.replace("путін", "хуй")
    if cleaned_message != message.content:
        await message.delete()
        await message.channel.send(cleaned_message)

    await bot.process_commands(message)  # Виклик обробника повідомлень

# Запуск бота
bot.run('MTIwOTIyMzE5ODE2ODg1MDU0Mw.GhYcUi.OmbVxBezt6sLKweMuti4-icHcGStEeg4xZv8t0')