
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bc

app = ApplicationBuilder().token("your_key").build()

app.add_handler(CommandHandler("hi", bc.hi))
app.add_handler(CommandHandler("add", bc.add_contact))
app.add_handler(CommandHandler("read", bc.read_contact))
app.add_handler(CommandHandler("del", bc.del_contact))
app.add_handler(CommandHandler("imp_exp", bc.imp_exp_contacts))
app.add_handler(CommandHandler("help", bc.help))


print('Server start')
app.run_polling()