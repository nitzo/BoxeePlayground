import mc


def playVideo():
	mc.ActivateWindow(14001)
	item = mc.ListItem(mc.ListItem.MEDIA_VIDEO_CLIP)
	item.SetPath('/media/unnamed/1.mp4')
	item.SetContentType('video/mp4')
	mc.GetPlayer().PlayInBackground(item)
	
	
	

