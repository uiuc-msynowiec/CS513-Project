#@begin W1_Outer_Workflow
#@in Menu.csv
#@in MenuItem.csv
#@out MenuItem_cleaned.csv
#@out Menu_cleaned.csv
#@out Menu_cleaned_2.csv
#@out avg_price_by_year.png

#@begin CleanMenu1
#@desc Clean and generate place_cleaned and clean currency.
#@in Menu.csv
#@out Menu_cleaned.csv
#@end CleanMenu1

#@begin CleanMenu2
#@desc Generate year and clean/generate year_cleaned
#@in Menu_cleaned.csv
#@out Menu_cleaned_2.csv
#@end CleanMenu2

#@begin RemoveNullZeroPrices
#@desc Remove rows with null or 0 prices
#@in MenuItem.csv
#@out MenuItem_cleaned.csv
#@end RemoveNullZeroPrices

#@begin CreateDBForSQL
#@in menupages.csv
#@in Menu_cleaned_2.csv
#@in MenuItem_cleaned.csv
#@out NYPL.db
#@desc Create DB to use SQL qauries
#@end ICViolationCheck

#@begin CreateDBTables
#@in NYPL.db
#@out Cleaned_menu
#@out Cleaned_menuitems_w_ic
#@out Cleaned_menupages
#@desc Create DB tables 
#@end CreateDBTables


#@begin ICViolationCheck
#@desc Remove IC Violations using SQL
#@in Cleaned_menuitems_w_ic
#@in Cleaned_menupages
#@out Cleaned_menupages(ICRemoved)
#@out Cleaned_menuitems
#@end ICViolationCheck

#@begin GetDiagnosticSummary
#@in Cleaned_menu
#@in Cleaned_menuitems_w_ic
#@in Cleaned_menupages(ICRemoved)
#@in Cleaned_menuitems
#@out CleaningDiagnosticSummary
#@desc GetDiagnosticSummary
#@end GetDiagnosticSummary

#@begin GetICViolationSummary
#@in Cleaned_menuitems_w_ic
#@in Cleaned_menupages(ICRemoved)
#@in Cleaned_menuitems
#@out IcViolationSummary
#@desc GetICViolationSummary
#@end GetICViolationSummary

#@begin GetPriceVizSummary
#@in IcViolationSummary
#@in CleaningDiagnosticSummary
#@out PriceVisualization
#@desc GetPriceVizSummary
#@end GetPriceVizSummary


#@begin VisualizePriceTrend
#@desc Plot average menu item price per year
#@in PriceVisualization
#@out avg_price_by_year.png
#@out avg_price_by_year_and_state.png
#@end VisualizePriceTrend

#@end W1_Outer_Workflow