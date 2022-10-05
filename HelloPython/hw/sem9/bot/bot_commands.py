from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import controller as c


async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')


async def add_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    contact = update.message.text
    user_list = contact.split()
    c.WriteNumber(user_list[1], user_list[2], user_list[3])
    await update.message.reply_text(f'You add:{user_list[1]} {user_list[2]}')

async def read_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    contact = update.message.text
    user_list = contact.split()
    if len(user_list) == 3:
        await update.message.reply_text(f'You contacts is: {c.ReadNumber(user_list[1], user_list[2])}')
    else:
        for n in c.ReadNumber(user_list[1]):
            await update.message.reply_text(f'You contacts is: {n}')
    
async def del_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    contact = update.message.text
    user_list = contact.split()
    c.DelContact(user_list[1], user_list[2])
    await update.message.reply_text('Contaсt was deleted!')
    
async def imp_exp_contacts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    contact = update.message.text
    user_list = contact.split()
    c.ImportExport(user_list[1], user_list[2])
    await update.message.reply_text('Copied!')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('/hi')
    await update.message.reply_text('/add name phone filename')
    await update.message.reply_text('/read filename name - if you want one contact')
    await update.message.reply_text('/read filename - if you want all contacts')
    await update.message.reply_text('/del name filename')
    await update.message.reply_text('/imp_exp filename_from filename_to')
