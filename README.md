# Real World Effectiveness of COVID-19 Vaccines across Several Countries
Coronavirus Disease 2019 (COVID-19) has affected millions of people around the globe. However, with the increased availability of vaccination, the cases across the regions have started to drop. Different parts of the world are using different vaccines due to availability, costs, political and other reasons. For example, Chile, Bahrain and United Arab Emirates (UAE) are predominately administering inactivated virus vaccines, which use a form of the virus that has been inactivated. On the other hand, Israel and United States (US) mostly are employing messenger RNA, or mRNA vaccines, that work by sending mRNA signals to trigger the immune response. United Kingdom is using viral vector vaccines, which use a genetically engineered virus to carry the genetic code to generate a protein that prompts an immune response. While, Hungary remains hybrid and currently administering both vector and inactivated vaccines. While the vaccines differ in their working principle, all of them showed promising results in the clinical trials. Here we use the real-world evidence data of COVID 19 cases and deaths across the highly vaccinated countries to get insights into the performance of these vaccine and compare the efficacy and effectiveness of these vaccines in a real-world setting.

## Methods
The COVID-19 data for new cases, death and vaccines administered between December 14th, 2020 (first day of the vaccine roll out) and May 30th, 2021 was sourced programmatically from “Our World in Data COVID-19 dataset” [1]. To remove daily fluctuations in the new cases and deaths, the moving average filter of fourteen days was applied [2]. To estimate relative in new cases and deaths, the smoothed time series were normalized with respect to the mean number of new cases and deaths between December 14th, 2020 to January 24th, 2021 respectively. This six week window for normalization was selected to smooth out any short term variation in the COVID cases. Finally, these normalized time series were plotted against COVID-19 vaccine doses administered per 100 people.
