from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ActivationTokenGenerator(PasswordResetTokenGenerator):
	#	def _make_token_with_timestamp(self, user, timestamp):
	#		return (str(user.pk)+str(timestamp)+str(user.is_active))
	pass


account_activation_token = ActivationTokenGenerator()
