# آزمایش اول - آزمایشگاه مهندسی نرم‌افزار
اعضای گروه: امیرحسین ندایی پور، علی مهربانی

## گزارش روال انجام آزمایش
### ایجاد مخزن، فایل .gitignore، فایل README و قالب اولیه کد
بعد از ایجاد مخزن، آن را روی دستگاه خود clone کردیم و مشاهده می‌کنید که فولدر .git هم ساخته شده است:
<img width="960" alt="1clone-dotgit" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/d75fdc8d-8e37-41da-964d-5a7cb8c78507">

در مراحل بعدی فایل .gitignore را ساختیم و محتویات پوشه report-images را که شامل screenshot های استفاده شده در همین گزارش است را ignore کردیم تا به مخزن remote افزوده نشوند:
<img width="960" alt="2gitignore" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/0d29cb21-1434-409a-b101-5c2fcbb85d5b">

<img width="960" alt="3ignore-report-images" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/e88ab2ed-52b0-4bdd-83ee-54c0b535353a">

<img width="960" alt="3commit-gitignore" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/870a72c3-ca07-4803-8f36-1472f7e803df">

در مرحله بعد فایل README را به پروژه افزودیم تا بعد از انجام پروژه گزارش را در آن تکمیل کنیم:
<img width="960" alt="4readme" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/4f57e212-dea5-407b-a7ac-e8d4fe2fb636">

سپس بدنه اصلی برنامه را در فایل main.py ساختیم که شامل دو تابع پیاده‌سازی نشده بود که در ادامه توسط دو عضو گروه در دو شاخه جداگانه توسعه داده می‌شوند:
<img width="960" alt="6main" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/23fbc67c-e6a9-4891-ace3-e2226e01bb17">

در نهایت هم برای محافظت از شاخه master یک rule به آن اضافه می‌کنیم که توسعه‌دهندگان را ملزم می‌کند قبل از مرج با master یک pull request ثبت کنند:
<img width="960" alt="0pull-request" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/c7d541a2-477e-4b35-a8dd-da3ab7c82312">

### ایجاد شاخه dev، توسعه و merge آن
ابتدا شاخه dev-fibonacci را که قرار است روی آن تابع fibonacci پیاده‌سازی شود، ایجاد می‌کنیم:
<img width="960" alt="8branch" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/c98f7bc4-79dd-473c-aaac-8e2d2d7cfb76">

سپس روی این شاخه تابع fibonacci را پیاده‌سازی می‌کنیم:
<img width="960" alt="9fibonacci" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/06a8b406-a411-4740-9a33-418ca25cf48a">

در نهایت تغییرات را commit و push می‌کنیم:
<img width="960" alt="10publish-fibonacci" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/b8f4b9a6-8f05-46a6-9297-583821b07caa">

حالا در مخزن پروژه یک pull request ثبت می‌کنیم تا پیاده‌سازی انجام شده روی این شاخه با شاخه master مرج شود:
<img width="960" alt="11pull-request-fibonacci" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/ebb962a2-b855-41df-8a54-e3f20ea624fe">

در نهایت بعد از دریافت approval از توسعه‌دهنده دیگر پروژه (مطابق تنظیمات rule ساخته شده) شاخه dev با master مرج می‌شود:
<img width="960" alt="12approval" src="https://github.com/nedaei79/SEL-Week1/assets/62210316/d3b1f2cf-2bc2-49b5-930a-edcc9c7e7d69">


### ایجاد شاخه feature، توسعه و merge آن
برای تغییر نحوه print کردن خروجی یک شاخه جدید به نام feature-print را به صورت زیر ایجاد می‌کنیم. این شاخه پیش از merge شدن شاخه dev ایجاد شده است:
![create-feature-branchpng](https://github.com/nedaei79/SEL-Week1/assets/59169318/9992ec52-2a25-40ab-be2c-6516b12c279e)

سپس کد مورد را پیاده‌سازی کرده و commit می‌کنیم:
![implement-pretty-print-commit](https://github.com/nedaei79/SEL-Week1/assets/59169318/eb60fabc-9eef-441b-970d-9b1c0765fa78)

و در نهایت شاخه جدید را بر روی remote پوش می‌کنیم:
![push-feature-print-2origin](https://github.com/nedaei79/SEL-Week1/assets/59169318/d82a120b-a117-4611-9a53-cf4226560d2d)

بعد از این کار شاخه dev مرج می‌شود که در بخش قبل مشاهده کردیم. پس از آن به صورت زیر pull request برای شاخه feature ایجاد می‌شود:
![pull-req-feature-print](https://github.com/nedaei79/SEL-Week1/assets/59169318/38cfe3ee-15d0-4e08-85d9-652f97dfe3c3)

همانطور که مشاهده می‌کنیم به دلیل merge شدن شاخه dev باید conflict موجود را ابتدا برطرف کنیم. برای این کار شاخه master را pull می‌کنیم و به صورتی که در سه تصویر زیر مشاهده می‌کنیم conflict را برطرف کرده و تغییرات را push می‌کنیم:
![resolve-print-conf](https://github.com/nedaei79/SEL-Week1/assets/59169318/ef4d2a6d-dae0-4ac9-9e68-a06b75eee16a)

![before-resolve-print-conf](https://github.com/nedaei79/SEL-Week1/assets/59169318/12f8f518-faa4-488e-bc29-db979a77461e)

![print-conf-after-res](https://github.com/nedaei79/SEL-Week1/assets/59169318/f196cf1a-6665-464f-99b8-f388e2d7c733)

در نهایت وضعیت pull request در github تغییر کرده و آن را approve می‌کنیم.

### ایجاد تغییر مختصر با هدف برخوردن به conflict دوم

برای ایجاد conflict دوم ابتدا جای تو تابع موجود در فایل main.py را تغییر می‌دهیم و بر روی شاخه master پوش می‌کنیم. در همین حین فرد توسعه‌دهنده دیگر بدون pull کردن یک کامنت به تایع print result اضافه می‌کند و تلاش می‌کند آن را بر روی remote پوش کند اما با خطا روبرو می‌شود:
![change-and-runinto-conf](https://github.com/nedaei79/SEL-Week1/assets/59169318/39173f9b-2ea5-415e-8a2a-601022b407bb)

در ادامه برای برطرف کردن آن ابتدا تغییرات را از remote بر روی شاخه اصلی pull می‌کنیم و سپس همانطور که در سه تصویر زیر مشاهده می‌کنیم conflict را برطرف کرده و تغییرات را commit می‌کنیم:
![commit-resolve-2nd-conf](https://github.com/nedaei79/SEL-Week1/assets/59169318/efa6ed72-1c75-4392-b7e5-f1c5a70f4e66)

![before-resolve-2nd-conf](https://github.com/nedaei79/SEL-Week1/assets/59169318/7917f090-8d0e-4222-b961-73cbb6a44285)

![after-resolve-2nd-conf](https://github.com/nedaei79/SEL-Week1/assets/59169318/1a6bebe5-8b86-4841-a20d-20284a45d9bc)


## پاسخ پرسش‌ها
### پرسش یک

پوشه .git پوشه‌ای است که گیت در آن همه اطلاعات مربوط به تغییرات کد را ثبت می‌کند. این پوشه با اجرای دستور git init ساخته می‌شود و محتویات آن به طور خلاصه شامل موارد زیر است:
- فایل HEAD که شاخه‌ای که روی آن قرار داریم را ذخیره می‌کند.
- پوشه refs که reference های همه شاخه‌ها و commit ها را ذخیره می‌کند.
- پوشه objects که کد ما را در قالب تعدادی snapshot نگه‌داری می‌کند.
- فایل config که اطلاعات پیکربندی گیت را نگه می‌دارد.
- پوشه hooks که قطعه کدهایی که قرار است در زمان‌های خاصی از کار با گیت اجرا شوند را نگه می‌دارد. مثلا قطعه کدی که قبل از هر push اجرا می‌شود یا شبیه این.

### پرسش دو

منظور از atomic commit این است که تغییرات موجود در هر commit تا جای ممکن کوچک باشد و بتوان آن را کاملا ساده در حد یک جمله در همان commit کامنت کرد. این کار به واضح بودن تغییرات اعمال شده در هر commit برای توسعه دهندگان کمک می‌کند. مشابه آن، مفهوم atomic pull request را داریم که به معنی حداقلی بودن تغییرات موجود در هر pull request است، به صورتی که بتوان تغییرات را در چند دقیقه مرور کرد. با این کار تغییرات موجود برای reviewer گیج‌کننده نخواهد بود و فهم آن را راحت‌تر می‌کند.

### پرسش سه

- دستور fetch تنها لیست تغییرات موجود در مخزن remote (یعنی مخزن آنلاین) را به اطلاع مخزن محلی می‌رساند ولی خود تغییرات اعمال نمی‌شوند و کد محلی دست نخورده می‌ماند.
- درحالی که دستور pull علاوه بر این کار خود تغییرات را هم از مخزن آنلاین به مخزن محلی می‌آورد و کد محلی را تغییر می‌دهد.
- دستور git merge target-branch تغییرات کد شاخه‌ای به نام target-branch را در قالب یک commit به شاخه‌ای که روی آن قرار داریم می‌آورد و تاریخچه commit در شاخه target-branch را هم به شاخه حاضر انتقال می‌دهد.
- دستور git rebase target-branch feature-branch بر خلاف مرج، تغییرات کد را از شاخه target-branch به feature-branch نمی‌آورد بلکه کامیت‌های انجام شده روی feature-branch را از آخرین باری که از شاخه target-branch جدا شده در نظر می‌گیرد، آن‌ها را به ترتیب روی وضعیت حال حاضر target-branch اعمال می‌کند و تاریخچه target-branch را هم به جای تاریخچه feature-branch قرار می‌دهد.
- با دستور git cherry-pick c1 کامیت با آیدی c1 که ممکن است روی شاخه دیگری هم باشد، روی وضعیت حال حاضر شاخه‌ای که روی آن قرار داریم اعمال می‌شود. دستور git cherry-pick feature-branch هم تنها کامیت آخر از شاخه feature-branch را بر می‌دارد و روی شاخه حاضر اعمال می‌کند.

### پرسش چهار

هر سه دستور اشاره شده به ما کمک می‌کنند تغییرات ناخواسته ایجاد شده را اصلاح کنیم. اما به صورت خلاصه عملکرد هر دستور به این صورت است:

- دستور reset: این دستور به ما کمک می‌کند HEAD را به صورتی جابجا کنیم که commitهایی را به شاخه اضافه یا از آن حذف کنیم. در نتیجه این دستور در تاریخچه commitها تغییر ایجاد می‌کند.
- دستور restore: این دستور به ما کمک می‌کند فایل‌هایی را که به اشتباه staged شده‌اند را از این وضعیت خارج کنیم. این دستور در برخی حالات می‌تواند موجب از دست رفتن تغییرات اعمال شده در فایل‌ها شود و همچنین تاریخچه شاخه را تغییر نمی‌دهد.
- دستور revert: این دستور به ما کمک می‌کند تا تغییرات اعمال شده در commitهای دلخواه گذشته را در قالب یک commit جدید به حالت قبل برگردانیم. در نتیجه این دستور تاریخچه commitها را تغییر نمی‌دهد.

### پرسش پنج

مفهوم stage به توسعه‌دهنده کمک می‌کند فقط بخشی از تغییرات محلی خود را کامیت کند. به عبارت دیگر تنها تغییرات stage شده کامیت می‌شوند و برای اضافه کردن فایل‌ها به stage هم از دستور git add file-name استفاده می‌شود.
دستور git stash هم همه تغییراتی که کامیت نشده‌اند را ذخیره می‌کند و بعدا می‌شود با دستور git stash pop این تغییرات را برگرداند. کاربرد آن برای مثال در زمانی است که می‌خواهیم pull کنیم اما با پیامی مواجه می‌شویم که از ما میخواهد اول تغییرات محلی‌مان را کامیت کنیم. اگر تغییرات محلی ما در حدی نباشد که یک کامیت معنادار و بدون باگ را شکل دهد، می‌توانیم تغییرات را stash کنیم، pull کنیم و در نهایت stash pop کنیم و به تغییر کد محلی از همان جایی که آن را ذخیره کرده بودیم، ادامه دهیم.

### پرسش شش

  منظور از snapshot، وضعیت فایل‌های مخزن در هر مرحله از توسعه آن‌هاست. در واقع ما با ایجاد تغییر و commit کردن آن‌ها، فایل‌های مخزن را از یک وضعیت، به وضعیتی جدیتر می‌بریم. در نتیجه هر commit نشان‌دهنده یک snapshot از وضعیت فایل‌های مخزن است که می‌توان به آن ارجاع داد.
