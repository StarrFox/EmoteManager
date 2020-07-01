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
import traceback

import discord
from bot_bin.bot import Bot
from discord.ext import commands

logging.basicConfig(level=logging.WARNING)
logging.getLogger('discord').setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Bot(Bot):
	startup_extensions = (
		'cogs.emote',
		'cogs.meta',
		'cogs.stats',
		'bot_bin.debug',
		'bot_bin.misc',
		'bot_bin.systemd',
		'jishaku',
	)

	def __init__(self, **kwargs):
		with open('data/config.py') as f:
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
	import sys

	kwargs = dict(guild_subscriptions=False, request_offline_members=False)

	if len(sys.argv) < 3:
		print('Usage:', sys.argv[0], '<shard count> <hyphen-separated list of shard IDs>', file=sys.stderr)
		sys.exit(1)

	shard_count = int(sys.argv[1])
	shard_ids = list(map(int, sys.argv[2].split('-')))
	Bot(**kwargs, shard_count=shard_count, shard_ids=shard_ids).run()

if __name__ == '__main__':
	main()
