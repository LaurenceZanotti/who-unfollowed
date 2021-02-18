// This is a utility script used in the browser console to retrieve datasets.
// Maybe a webcrawler might be implemented in the future

/**
 * Gets an array of followers from IG div element
 * (only works if the div was scrolled all the way down, loading all accounts to the DOM)
 */
function getFollowers() {
	let igs = document.querySelectorAll('.FPmhX')
	let nicknames = []

	for (let ig of igs) {
		nicknames.push(ig.innerText)
	}
	
	return nicknames
}


/**
 * Returns a formatted array in either stringified JSON format or txt with newlines
 * @param {object} arr - The followers array
 * @param {string} format - The format which the followers will be formatted to
 */
function formatFollowers(arr, format) {
	// Ensure arr is an array
	if (!arr || typeof(arr) != "object") {
		throw TypeError("Must provide an array of accounts")
	}
	// Returns specified format
	if (format === 'json') {
		return JSON.stringify(arr)
	} else if (format === 'txt') {
		return arr.join('\n')
	}
	// Throws error if format has unsupported value and type
	else {
		throw Error('Must choose format between json or txt')
	}
}

// Get array of accounts
let accounts = getFollowers()
let accounts_json = formatFollowers(accounts, 'json')
let accounts_txt = formatFollowers(accounts, 'txt')

// Use console.log() within account_json or account_txt vars to display data to console
// Then just copy to a json or txt file to use within the program