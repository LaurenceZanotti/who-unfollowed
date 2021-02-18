// Este é um script de utilidade usado no console do navegador para buscar datasets.
// Talvez um webcrawler seja implementado no futuro

/**
 * Obtém um array de seguidores do elemento div do IG
 * (funciona apenas se a div tiver sido scrollada até o final, carregando todas as contas
 * no DOM)
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
 * Retorna um array formatado em formato JSON stringificado ou txt com newlines
 * @param {object} arr - O array de seguidores
 * @param {string} format - O formato que os seguidores serão convertidos
 */
function formatFollowers(arr, format) {
	// Garantir que arr é um array
	if (!arr || typeof(arr) != "object") {
		throw TypeError("Precisa providenciar um array com contas do IG")
	}
	// Retorna o formato especificado
	if (format === 'json') {
		return JSON.stringify(arr)
	} else if (format === 'txt') {
		return arr.join('\n')
	}
	// Lança erro se o formato tiver um valor e tipo não suportado
	else {
		throw Error('Precisa escolher um formato entre json ou txt')
	}
}

// Obter array de contas
let accounts = getFollowers()
let accounts_json = formatFollowers(accounts, 'json')
let accounts_txt = formatFollowers(accounts, 'txt')

// Use console.log() com as variáveis account_json ou account_txt para exibir os dados no console
// E então apenas copie para um arquivo json ou txt para usar com o programa