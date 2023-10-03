# Cat-Emotion-Detection
Using custom Yolov5 object detection model to recognize emotion of cats.


## 目錄
- [背景與動機](#題目發想)
- [功能說明](#功能說明)


## 背景與動機
貓咪是世界上最受歡迎的寵物之一，許多人將貓咪視為親生子女般照顧及陪伴，時刻關心著它們的身心狀況，飼主們除了定期帶它們去做身體檢查，也常常為了討貓咪歡心而購買各種玩具或零食，更花時間每天親自陪貓咪玩耍，然而，貓咪的情緒及個性捉摸不定，時常讓飼主們感到疑惑不已，因此，為了讓飼主可以了解自己的貓咪目前情緒的狀態，本專題利用貓咪臉部的動作來判斷貓咪目前的情緒是處於正面、中立或是負面，以輔助飼主進行判斷。

## 功能說明
本專題提供使用者圖形介面，方便使用者進行操作，如下圖所示：

<div align = "center">
<img src = "https://i.imgur.com/yoFnkxI.png" width = 350px>
</div>

使用者可以選擇上傳貓咪的圖片、影片或使用攝像頭直接進行拍攝，若是使用圖片或影片的功能，電腦辨識完圖片及影片之後會在視窗的右上方顯示 "Process successfully" 以提醒使用者，這時按下下方的 result 按鈕後便可瀏覽辨識好的圖片或影片，而若是使用攝像頭的功能，則可以進行即時辨識。
<br>
若貓咪被判斷為負面情緒，則會產生負面情緒的標記匡，正面則會產生正面情緒的標記匡，中立則會產生中立情緒的標記匡，如下所示：

負面情緒：

<div align = "center">
<img src = "https://i.imgur.com/k49wrWK.jpg" width = 300px>
</div>

正面情緒：

<div align = "center">
<img src = "https://i.imgur.com/2Hvp5Yc.jpg" width = 300px>
</div>

中立情緒：

<div align = "center">
<img src = "https://i.imgur.com/5N3VLQv.jpg" width = 300px>
</div>
