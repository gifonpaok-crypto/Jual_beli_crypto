from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = 9038628620:AAGuim0lpJ3WiFrNqKF_ixOB-x-Oud_pTeU
user_lang = {}

def teks_menu(nama, lang="id"):
    if lang=="id":
        return f"🏠 *Menu Utama Jual Beli Crypto*\nHallo : {nama}\n--------------------------------\nPilih salah satu menu di bawah ini:"
    else:
        return f"🏠 *Main Menu Jual Beli Crypto*\nHello : {nama}\n--------------------------------\nChoose one menu below:"

def keyboard_menu(lang="id"):
    if lang=="id":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("🛒 Beli Crypto", callback_data="beli"),
             InlineKeyboardButton("🅿️ Jual Crypto", callback_data="jual")],
            [InlineKeyboardButton("🔄 Swap/Bridge", callback_data="swap"),
             InlineKeyboardButton("💎 Stars & Premium", callback_data="stars")],
            [InlineKeyboardButton("💳 Check Stock", callback_data="stock"),
             InlineKeyboardButton("🧾 List Fee", callback_data="fee")],
            [InlineKeyboardButton("👤 Profil", callback_data="profil")],
        ])
    else:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("🛒 Buy Crypto", callback_data="beli"),
             InlineKeyboardButton("🅿️ Sell Crypto", callback_data="jual")],
            [InlineKeyboardButton("🔄 Swap/Bridge", callback_data="swap"),
             InlineKeyboardButton("💎 Stars & Premium", callback_data="stars")],
            [InlineKeyboardButton("💳 Check Stock", callback_data="stock"),
             InlineKeyboardButton("🧾 List Fee", callback_data="fee")],
            [InlineKeyboardButton("👤 Profile", callback_data="profil")],
        ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teks = "🇮🇩 Pilih Bahasa anda\n🇺🇸 Select your language"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🇮🇩 Indonesia", callback_data="lang_id"),
         InlineKeyboardButton("🇺🇸 English", callback_data="lang_en")]
    ])
    await update.message.reply_text(teks, reply_markup=keyboard)

async def tombol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    await query.answer()
    data = query.data
    if data=="lang_id":
        user_lang[user.id]="id"
        await query.message.reply_text("✅ Bahasa diubah ke Indonesia")
        await query.message.reply_text(teks_menu(user.first_name,"id"), reply_markup=keyboard_menu("id"), parse_mode="Markdown")
    elif data=="lang_en":
        user_lang[user.id]="en"
        await query.message.reply_text("✅ Language changed to English")
        await query.message.reply_text(teks_menu(user.first_name,"en"), reply_markup=keyboard_menu("en"), parse_mode="Markdown")
    elif data=="beli":
        await query.message.reply_text("🛒 *BELI CRYPTO*\n\nMinimal Rp5.000\n\nKetik: /beli USDT 50000\nContoh: Beli USDT Rp50.000\n\nChat Admin untuk order: @username_lu", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Kembali", callback_data="back_menu")]]))
    elif data=="jual":
        await query.message.reply_text("🅿️ *JUAL CRYPTO*\n\nMinimal Rp5.000\n\nChat Admin untuk order: @username_lu", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Kembali", callback_data="back_menu")]]))
    elif data=="swap":
        await query.message.reply_text("🔄 *SWAP & BRIDGE*\n\nMinimal Rp1.000\nNO FEE mulai Rp1.000 - Rp20.000", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Kembali", callback_data="back_menu")]]))
    elif data=="stars":
        await query.message.reply_text("💎 *STARS & PREMIUM*\n\n• 50 Stars = Rp15.000\n• 100 Stars = Rp29.000\n• Premium 1 Bulan = Rp45.000", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Kembali", callback_data="back_menu")]]))
    elif data=="stock":
        await query.message.reply_text("💳 *CHECK STOCK*\n\n• USDT : Rp50.000.000\n• TON : 500 TON\n• BTC : 0.01 BTC\n• ETH : 1 ETH", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Kembali", callback_data="back_menu")]]))
    elif data=="fee":
        await query.message.reply_text("🧾 *LIST FEE*\n\n• Beli : 2%\n• Jual : 2%\n• Swap Rp1.000-Rp20.000 : NO FEE\n• Swap > Rp20.000 : 1%\n\nInvite Teman Dapet Rp1.000 / temen VALID\nDapet 10% dari fee transaksi temen lu!", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Kembali", callback_data="back_menu")]]))
    elif data=="profil":
        await query.message.reply_text(f"👤 *PROFIL*\n\nNama: {user.first_name}\nID: {user.id}\nUsername: @{user.username}\nTotal Transaksi: 0\nTotal Referral: 0\nSaldo Komisi: Rp0", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Kembali", callback_data="back_menu")]]))
    elif data=="back_menu":
        lang=user_lang.get(user.id,"id")
        await query.message.reply_text(teks_menu(user.first_name,lang), reply_markup=keyboard_menu(lang), parse_mode="Markdown")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(tombol))
print("Bot Jual Beli Crypto udah jalan...")
app.run_polling()
