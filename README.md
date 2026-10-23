# Prefect Bots — GitHub و Render

## مهم: امنیت
کلیدها و توکن‌های داخل نسخه اولیه از کد حذف شده‌اند و باید در Render به‌صورت Environment Variables تنظیم شوند. چون نسخه اولیه حاوی اطلاعات محرمانه بوده، توکن ربات‌های بله و کلیدهای API را از پنل سرویس مربوطه عوض/باطل کنید و کلیدهای جدید بسازید. کلید واقعی را در GitHub قرار ندهید.

## انتشار در GitHub
1. فایل ZIP را باز کنید.
2. در GitHub یک repository جدید بسازید.
3. تمام فایل‌های این پوشه، از جمله `render.yaml` و `requirements.txt` را در ریشه repository بارگذاری و Commit کنید.
4. repository را Public نکنید مگر اینکه مطمئن شوید هیچ داده محرمانه‌ای در آن نیست.

## استقرار در Render
1. در Render گزینه **New + → Blueprint** را انتخاب و repository را وصل کنید.
2. Render تنظیمات `render.yaml` را می‌خواند. برای هر ربات، متغیرهای محیطی خواسته‌شده را با مقادیر جدید وارد کنید.
3. سرویس‌ها را Deploy کنید و لاگ هر Worker را بررسی کنید.

این Blueprint می‌سازد چهار Background Worker مجزا؛ Background Workers در Render معمولاً به پلن پولی نیاز دارند. برای ربات‌های دائمی از Web Service استفاده نکنید مگر اینکه کد برای آن تغییر داده شود.

## متغیرهای محیطی
- `prefect-gersha`: `BALE_TOKEN`, `GAPGPT_API_KEY`
- `prefect-gpt-bale`: `BOT_TOKEN`, `OPENAI_API_KEY`, `GEMINI_API_KEY`, `OWEN_API_KEY`, `GROQ_API_KEY`
- `prefect-video-downloader`: `BOT_TOKEN`
- `prefect-khabar`: `BALE_BOT_TOKEN`

اگر یک سرویس به کلید خاصی نیاز ندارد، مقدارش را تنظیم نکنید؛ اما اگر برنامه هنگام شروع آن را اجباری می‌داند، باید کلید معتبر وارد شود.

## نکته
فایل‌های SQLite روی دیسک موقت Render ممکن است بعد از restart/deploy از بین بروند. برای نگه‌داری پایدار داده‌ها، دیسک پایدار یا پایگاه داده خارجی لازم است.
