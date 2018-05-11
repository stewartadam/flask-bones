from flask_failsafe import failsafe

@failsafe
def create_app_safe():
  from app import create_app, config
  return create_app(config.dev_config)

app = create_app_safe()
