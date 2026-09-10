# generating csv file automatically

csv_content = """Order_ID,Product,Category,Price,Quantity,Discount
1001,MacBook Pro,Electronics,1999.99,1,0.0
1002,Office Chair,Furniture,149.50,3,0.1
1003,Coffee Maker,Appliances,89.99,2,0.0
1004,Bluetooth Headphones,Electronics,79.99,5,0.15
1005,Desk Lamp,Furniture,34.99,4,0.0
1006,Blender,Appliances,49.99,2,0.0
1007,iPhone 15,Electronics,999.99,1,0.05
1008,Standing Desk,Furniture,399.99,1,0.1
1009,Toaster,Appliances,29.99,3,0.0
1010,Wireless Mouse,Electronics,24.99,10,0.2
1011,Bookshelf,Furniture,125.00,2,0.0
1012,Air Fryer,Appliances,119.99,1,0.0
1013,4K Monitor,Electronics,349.99,2,0.1
1014,Dining Table,Furniture,599.99,1,0.15
1015,Vacuum Cleaner,Appliances,179.99,2,0.0
1016,Gaming Keyboard,Electronics,89.99,3,0.0
1017,Office Desk,Furniture,249.99,1,0.0
1018,Microwave,Appliances,149.99,1,0.05
1019,USB-C Cable,Electronics,15.99,15,0.25
1020,Filing Cabinet,Furniture,89.99,2,0.0
1021,Slow Cooker,Appliances,59.99,4,0.1
1022,Tablet,Electronics,449.99,2,0.0
1023,Ergonomic Stool,Furniture,79.99,3,0.0
1024,Rice Cooker,Appliances,39.99,2,0.0
1025,External Hard Drive,Electronics,119.99,4,0.1
1026,Nightstand,Furniture,69.99,2,0.0
1027,Juicer,Appliances,99.99,1,0.0
1028,Mechanical Keyboard,Electronics,129.99,2,0.05
1029,Bookshelf,Furniture,125.00,1,0.0
1030,Food Processor,Appliances,,2,0.0
1031,Gaming Mouse,Electronics,59.99,5,0.1
1032,Office Chair,Furniture,149.50,100,0.3
1033,Toaster Oven,Appliances,79.99,1,0.0
1034,Smart Watch,Electronics,249.99,3,0.0
1035,Coffee Table,Furniture,179.99,1,0.1
1036,Electric Kettle,Appliances,34.99,5,0.0
1037,Bluetooth Speaker,Electronics,69.99,4,0.15
1038,Desk Lamp,Furniture,34.99,2,0.0
1039,Blender,Appliances,49.99,1,0.0
1040,Laptop Stand,Electronics,39.99,3,0.0
1041,Office Chair,Furniture,149.50,2,0.0
1042,Air Fryer,Appliances,,1,0.1
1043,HDMI Cable,Electronics,12.99,20,0.3
1044,Standing Desk,Furniture,399.99,2,0.0
1045,Coffee Maker,Appliances,89.99,3,0.0
1046,Wireless Earbuds,Electronics,149.99,2,0.05
1047,Filing Cabinet,Furniture,89.99,1,0.0
1048,Slow Cooker,Appliances,59.99,1,0.0
1049,4K Monitor,Electronics,349.99,1,0.0
1050,Dining Table,Furniture,599.99,1,0.2"""

# Write the string above into a physical CSV file named sales.csv
with open("sales.csv", "w") as file:
    file.write(csv_content.strip())
