package lasagna

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, averagePrepTime int) int {
	if averagePrepTime == 0 {
		averagePrepTime = 2
	}

	return averagePrepTime * len(layers)
}

// TODO: define the 'Quantities()' function
func Quantities(layers []string) (int, float64) {
	sauce := 0
	noodles := 0

	for _, item := range layers {
		if item == "noodles" {
			noodles++
		}
		if item == "sauce" {
			sauce++
		}
	}
	return noodles * 50, float64(sauce) * 0.2
}

// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendList, myList []string) {
	myList[len(myList)-1] = friendList[len(friendList)-1]
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantities []float64, scaleFactor int) []float64 {
	scaled := []float64{}
	for _, item := range quantities {
		// quantities[idx] *= float64(scaleFactor)
		scaled = append(scaled, item*float64(scaleFactor)/2)
	}
	return scaled
}
