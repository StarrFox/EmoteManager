#!/usr/bin/env python3

# © 2018–2020 io mintz <io@mintz.cc>
#
# Emote Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Emote Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Emote Manager. If not, see <https://www.gnu.org/licenses/>.

import base64
import logging

import discord
from bot_bin.bot import Bot

logging.basicConfig(level=logging.WARNING)
logging.getLogger('discord').setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Bot(Bot):
	startup_extensions = (
		'cogs.emote',
		'jishaku',
	)

	def __init__(self, **kwargs):
		with open('data/config.py', encoding='utf-8') as f:
			config = eval(f.read(), {})

		super().__init__(config=config, **kwargs)
		# allow use of the bot's user ID before ready()
		token_part0 = self.config['tokens']['discord'].partition('.')[0].encode()
		self.user_id = int(base64.b64decode(token_part0 + b'=' * (3 - len(token_part0) % 3)))

	def process_config(self):
		"""Load the emojis from the config to be used when a command fails or succeeds
		We do it this way so that they can be used anywhere instead of requiring a bot instance.
		"""
		super().process_config()
		import utils.misc
		default = ('❌', '✅')
		utils.SUCCESS_EMOJIS = utils.misc.SUCCESS_EMOJIS = (
			self.config.get('response_emojis', {}).get('success', default))

def main():
	Bot(
		intents=discord.Intents(
			guilds=True,
			# we hardly need DM support but it's helpful to be able to run the help/support commands in DMs
			messages=True,
			# we don't need DM reactions because we don't ever paginate in DMs
			guild_reactions=True,
			emojis=True,
			# everything else, including `members` and `presences`, is implicitly false.
		),
		chunk_guilds_at_startup=False,
		member_cache_flags=discord.MemberCacheFlags.none(),
		# disable message cache
		max_messages=None,
	).run()


if __name__ == '__main__':
	main()
