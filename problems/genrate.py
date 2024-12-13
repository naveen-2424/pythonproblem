import barcode
data="7639404343"
k=barcode.get_barcode_class('code128')
r=k(data)
r.save('barcode')