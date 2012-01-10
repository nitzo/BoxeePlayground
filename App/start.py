import mc
import counter

'''
here we can do some pre launch processing if we wish.
checking authentication or pre-loading content, anything we need.
'''

if mc.ShowDialogConfirm('Boxee Basic Python App', 'Would you like to launch the application?', 'No', 'Yes!'):
	mc.ActivateWindow(14000)
