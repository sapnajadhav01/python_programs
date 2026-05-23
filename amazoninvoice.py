#amazon invoice
cart=0;
cart=cart+1;
price=999.00;
total=cart*price;
discount=(total*15)/100;
final_bill=total-discount;
print(f"cart={cart},price={price}");
print(f"Discount={discount},final Amount={final_bill}");