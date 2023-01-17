package techpalace

import (
	"strings"
)

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
	return "Welcome to the Tech Palace, " + strings.ToUpper(customer)
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	sb := strings.Builder{}

	sb_pattern := strings.Builder{}
	for i := 1; i <= numStarsPerLine; i++ {
		sb_pattern.WriteString("*")
	}

	sb.WriteString(sb_pattern.String())
	sb.WriteString("\n")
	sb.WriteString(welcomeMsg)
	sb.WriteString("\n")
	sb.WriteString(sb_pattern.String())

	return sb.String()
}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
	newStr := strings.ReplaceAll(oldMsg, "*", "")
	secondStr := strings.Trim(newStr, " \n")
	return secondStr
}
