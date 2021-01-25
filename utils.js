// This is a utility script used in the browser console to retrieve datasets.
// Maybe a webcrawler might be implemented in the future

// Get followers in array format
function getFollowers() {
	igs = document.querySelectorAll('.FPmhX')
	nicknames = []

	for (ig of igs) {
		nicknames.push(ig.innerText)
	}
	
	return nicknames
}

// Print full array in JSON
console.log(JSON.stringify(nicknames))
