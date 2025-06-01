# Topic: 開放資料 - 水庫CTSI卡爾森指數
# File: 17_water_ctsi2.R
# Author: Ming-Chang Lee
# Date: 2025.06.01
# Data source: https://data.gov.tw/dataset/6345
# References: https://github.com/rwepa/python_data_scientist
# Python file: https://github.com/rwepa/teaching-programming/blob/main/17_water_ctsi.ipynb
# 說明: 本範例使用 readr, dplyr 套件

# 方法: 使用R {readr}, {dplyr} {tidyr} 套件

# 載入套件
library(readr) # read_csv 函數
library(dplyr) # mutate, filter, select 函數
library(tidyr) # pivot_wider 函數

# 匯入資料集
urls <- 'wqx_p_03.csv'
df <- read_csv(file=urls)
class(df) # "spec_tbl_df" "tbl_df" "tbl" "data.frame"

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
# 變數包括 num(實數), chr(字串),  logi(logical邏輯值)
# sampledate 欄位已經自動轉換為 POSIXct(日期時間)
str(df)

# itemvalue 為 chr(字串), 轉換為numeric
df <- df %>%
  mutate(itemvalue = as.numeric(itemvalue))
str(df$itemvalue) # num

# 資料摘要
# 資料有遺漏值(NA)
summary(df)

# 資料篩選: sampledepth = 0.5
df <- df %>%
  filter(sampledepth == 0.5) %>%
  select(sitename, itemname, itemvalue) %>%
  filter(complete.cases(.))

# 篩選資料, 考慮 temname = {葉綠素a, 總磷, 透明度, 卡爾森指數}
# 資料處理結果與Python操作相同
# https://github.com/rwepa/teaching-programming/blob/main/17_water_ctsi.ipynb

mydf <- df %>%
  filter(itemname %in% c('葉綠素a', '總磷', '透明度', '卡爾森指數'))
mydf
str(mydf) # 112*3

# 長寬資料轉換
# 使用 pivot_wider {tidyr} --> long data to wide data

mydf <- mydf %>%
  pivot_wider(names_from = itemname, values_from = itemvalue)

# 寬資料結果
df_wide # 28*5
# end
