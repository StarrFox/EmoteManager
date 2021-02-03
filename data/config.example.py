{
	'description':
		'Emote Manager lets you manage custom server emotes effortlessly.\n\n'
		'NOTE: Most commands will be unavailable until both you and the bot have the '
		'"Manage Emojis" permission.',
	'tokens': {
		'discord': 'sek.rit.token',
		},
	'prefixes': ["emp/"],
	'ignore_bots': {
		'default': True,
		'overrides': {
			'channels': [
			],
			'guilds': [
			],
		},
	},
	'copyright_license_file': 'data/short-license.txt',
	'socks5_proxy_url': None,  # required for connecting to the EC API over a Tor onion service
	'use_socks5_for_all_connections': False,  # whether to use socks5 for all HTTP operations (other than discord.py)
	'user_agent': 'EmoteManagerBotFork (https://github.com/StarrFox/EmoteManager)',
	'http_head_timeout': 10,  # timeout for the initial HEAD request before retrieving any images (up this if using Tor)
	'http_read_timeout': 60,  # timeout for retrieving an image
	# emotes that the bot may use to respond to you
	# If not provided, the bot will use '❌', '✅' instead.
	#
	# You can obtain these ones from the discordbots.org server under the name "tickNo" and "tickYes"
	# but I uploaded them to my test server
	# so that both the staging and the stable versions of the bot can use them
	'response_emojis': {
		'success': {  # emotes used to indicate success or failure
			False: '<:error:478164511879069707>',
			True: '<:success:478164452261363712>'
		},
	},
}
