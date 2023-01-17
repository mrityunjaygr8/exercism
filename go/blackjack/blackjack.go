package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	switch card {
	case "ace":
		return 11
	case "two":
		return 2
	case "three":
		return 3
	case "four":
		return 4
	case "five":
		return 5
	case "six":
		return 6
	case "seven":
		return 7
	case "eight":
		return 8
	case "nine":
		return 9
	case "ten", "jack", "queen", "king":
		return 10
	default:
		return 0
	}
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	v_1 := ParseCard(card1)
	v_2 := ParseCard(card2)
	v_d := ParseCard(dealerCard)
	sum := v_1 + v_2
	if v_1 == 11 && v_2 == 11 {
		return "P"
	}

	if sum == 21 {
		if v_d < 10 {
			return "W"
		}
		return "S"
	}

	if 17 <= sum && sum <= 20 {
		return "S"
	}

	if 12 <= sum && sum <= 16 {
		if v_d >= 7 {
			return "H"
		}
		return "S"
	}

	return "H"
}
