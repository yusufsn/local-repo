if (age>18) {
	//check loyalty card
	if (loyaltycard) {
		//give 30% discount
		price = price * 0.8;
	}
	can_watch = true;
}
return price;