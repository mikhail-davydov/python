import contextvars

ctx_user = contextvars.ContextVar('user')
ctx_user.set('admin')
