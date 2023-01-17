// Package weather will forecast the weather.
package weather

// CurrentCondition is the variable where the condition.
var CurrentCondition string

// CurrentLocation is the variable where the location.
var CurrentLocation string

// Forecast will forecast the weather.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
