#Introduction
Profil zaufany (Trusted profile) - is a free method of confirming the identity of a Polish citizen in electronic administration systems. In this case, it is an alternative to a paid qualified signature.

By comparing the obywatel.gov.pl website to the e-administration gate, thanks to which it is possible to submit applications, applications, complaints, fees and declarations to offices by electronic means without a personal visit to the office, the trusted profile itself should be compared to a personal key that allows every citizen using the e-services provided.

In order to obtain a trusted profile, you must submit an appropriate application via ePUAP, and then go with your ID card or passport to the confirmation point (ZUS, US, NFZ, UM). From October 2016, it is also possible to confirm the trusted profile through the transaction services of PKO Bank, inteligo, Santander, Bank Pekao, mBank, ING, Millennium Bank, Alior Bank, as well as through the Envelo platform. This form of confirmation does not require a personal appearance at the office or confirmation point.

After logging in to a trusted profile, you can view the list of confirmation points, which is not available anywhere else. In addition, it is not possible to display all points on the map in order to find the closest point. For this reason, I copied the table with addresses to an Excel file (it was not possible to fetch this data using the *requests* module) and slightly modified it, translating the addresses into English.

### Purpose of this app
I made this app for my grandma, who recently needed to obtain a trusted profile, but the list of confirmation points was so long, that she couldn't easily find the closest point. The only way to do this was to google addresses one by one.

With help came pandas and plotly, so data is read from xls file and then stored in a DataFrame and scattered on a map using plotly.

# Instruction
Just run *app.py* file