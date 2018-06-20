if (age>=18) {
	if (loyaltycard) {
		//give 30% discount
		price = price * 0.7;
	}
	can_watch = true;
}
return price;