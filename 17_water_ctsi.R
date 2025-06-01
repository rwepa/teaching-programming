# Topic: 開放資料 - 水庫CTSI卡爾森指數
# File: 17_water_ctsi.R
# Author: Ming-Chang Lee
# Date: 2025.06.01
# Data source: https://data.gov.tw/dataset/6345
# References: https://github.com/rwepa/python_data_scientist
# Python file: https://github.com/rwepa/teaching-programming/blob/main/17_water_ctsi.ipynb

# 方法1: 使用R的基本{stats}套件 - reshape 函數

# 匯入資料集
urls <- 'wqx_p_03.csv'
df <- read.table(file=urls, header=TRUE, sep=",")
class(df) # "data.frame"

# 顯示資料
# 測站名稱有29個
# 每筆記錄有25筆資料列(葉綠素a ~ 卡爾森指數)
# 每筆記錄包括一個以上 sampledepth = {0.5, 3.2, 7.6, ...}
# 湖山水庫二的第1筆資料為第 0列 ~ 第24列, sampledate = 2025/2/4  09:45:00 AM
# 湖山水庫二的第2筆資料為第25列 ~ 第24列, sampledate = 2025/2/4  09:45:00 AM
df

# 資料維度
dim(df) # 1000 19

# 欄位名稱
names(df)

# 資料型態
# 變數包括 int(整數), chr(字串), num(實數), logi(logical邏輯值)
str(df)

# itemvalue 為 chr(字串), 轉換為numeric
df$itemvalue <- as.numeric(df$itemvalue) # Warning message: NAs introduced by coercion 
str(df$itemvalue) # num

# 採樣日期(sampledate) 匯入資料為 object (字串), 轉換為日期時間(POSIXct).
df$sampledate <- as.POSIXct(df$sampledate)
str(df$sampledate) # POSIXct

# 資料摘要
# 資料有遺漏值(NA)
summary(df)

# 資料篩選: sampledepth = 0.5
df = df[df$sampledepth == 0.5, c('sitename', 'itemname', 'itemvalue')]
df # 725*3

# 刪除NA資料列
df <- na.omit(df) # 435*3

# 篩選資料, 考慮 temname = {葉綠素a, 總磷, 透明度, 卡爾森指數}
# 資料處理結果與Python操作相同
# https://github.com/rwepa/teaching-programming/blob/main/17_water_ctsi.ipynb
mydf <- df[(df$itemname == '葉綠素a') | (df$itemname == '總磷') | (df$itemname == '透明度') | (df$itemname == '卡爾森指數'),]
mydf
str(mydf) # 112*3

# 長寬資料轉換
# 使用 reshape {stats} --> long data to wide data
df_wide <- reshape(data = mydf,
                   timevar = "itemname",
                   idvar = "sitename",
                   direction="wide")

# 取代多餘的欄位名稱字元
names(df_wide) <- gsub(pattern = "itemvalue.", replacement = "", names(df_wide))

# 寬資料結果
df_wide
# end
