"""
Author: Mikhail Dorfman
Purpose: Development of High Throughput Cryogenics Imaging Assay Platform
"""

# this is the main part of our code, it contains the gui 
# all items are called from the gui, events trigger functions wirtten in other libraries/modules 

import wx
from wx.lib.masked import NumCtrl, EVT_NUM

from serial_com import temp_view, temp_set
from linear import linear_temp
from  shooter import shooting


class Interface(wx.Frame):
  
	def __init__(self, parent, title):
		style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER
		super(Interface, self).__init__(parent, title=title, 
			size=(400, 700), style=style)

		
		self.Centre()
		self.Show()  


		#//--output temp start  
		current_font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD) #font item for top
		st1 = wx.StaticText(self, label='Current Temperature:', pos=(30, 5)) #calls for "current temp" static text
		st1.SetFont(current_font) #sets the font for "current temp"

		#numeric box outputting current temp float
		out_current = wx.TextCtrl(self, pos=(250,8), size=(110,23))
		out_current.Enable(False)
		#out_temp = temp_view()
		#out_current.SetValue(out_temp)

		#//output temp end

		#style line below current temp
		wx.StaticLine(self, pos=(32,35), size=(335,1))


		#//--set temp area start

		sta = wx.StaticText(self, label='Set Temperature:', pos=(70,50))

		set_flt = NumCtrl(self, 
			pos=(240,50), size = (125,20),
			integerWidth = 2, fractionWidth = 2,
			min = -20.0, max = 20.0, limited = True, 
			autoSize = False)

		set_btn = wx.Button(self, label='Set!', pos=(160,85), size=(100,100))

		"""
		def tempset_click(event):
			val_in = set_flt.GetValue()
			temp_set(val_in)
		

                """
		set_btn.Bind(wx.EVT_BUTTON, tempset_click)

		#//set temp end

		title_font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		mode_font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

		#//--temp curve start

		temp_curve_title = wx.StaticText(self, label='Temperature Curve', pos=(125,150))
		temp_curve_title.SetFont(title_font)

		start_temp_label = wx.StaticText(self, label='Starting Temperature:', pos=(70, 185))
		start_temp_label.SetFont(mode_font)
		start_temp_flt = NumCtrl(self, 
			pos=(250,185), size = (125,20),
			integerWidth = 2, fractionWidth = 2,
			min = -20.0, max = 20.0, limited = True, 
			autoSize = False)


		final_temp_label = wx.StaticText(self, label='Final Temperature:', pos=(70, 220))
		final_temp_label.SetFont(mode_font)
		final_temp_flt = NumCtrl(self, 
			pos=(250,220), size = (125,20), 
			integerWidth = 2, fractionWidth = 2,
			min = -20.0, max = 20.0, limited = True, 
			autoSize = False)

		timed_temp_label = wx.StaticText(self, label='Time to Final:', pos=(70, 255))
		timed_temp_label.SetFont(mode_font)
		timed_temp_int = NumCtrl(self, pos=(250,255))




		#//--shooting mode starts

		shoot_mode_title = wx.StaticText(self, label='Shooting Mode', pos=(148,320))
		shoot_mode_title.SetFont(title_font)

		wx.StaticLine(self, pos=(105,345), size=(200,1))


		photo_instance_label = wx.StaticText(self, label='Photo Instantiation:', pos=(70, 365))
		photo_instance_label.SetFont(mode_font)

		shoot_duration_label = wx.StaticText(self, label='Shooting Duration:', pos=(70, 400))
		shoot_duration_label.SetFont(mode_font)


		photo_instance_int = NumCtrl(self, pos=(250,365))
		shoot_duration_int = NumCtrl(self, pos=(250,400))

		start_btn = wx.Button(self, label='Start', pos=(60,460))
		"""							       
		def start_click(event):
			#grab values from 5 nuemerical enteries
			y1 = start_temp_flt.GetValue()
			y2 = final_temp_flt.GetValue()
			x2 = timed_temp_int.GetValue()#first three go to linear_temp(x2, y1, y2)

 			linear_temp(x2, y1, y2)

			instantiation = photo_instance_int.GetValue()
			duration = shoot_duration_int.GetValue()#last two go to shooting(instantiation, duration)

			shooting(instantiation, duration)
		

                """
		start_btn.Bind(wx.EVT_BUTTON, start_click)
		


		stop_btn = wx.Button(self, label='Stop', pos=(240,460), size=(100,100))


		wx.StaticLine(self, pos=(105,500), size=(200,1))

		#//shooting mode end



		"""
		chk1 = wx.CheckBox(self, -1, "System running", pos=(140,360))
		chk1.Enable(False)
		run = False
		chk1.SetValue(run)


		st5 = wx.StaticText(self, label='Time:', pos=(70, 400))
		st5.SetFont(mode_font)
		"""
			

		self.Show()

#print Interface.tempset_click()

if __name__ == '__main__':
  
	app = wx.App()
	Interface(None, title='Mission Control')
	app.MainLoop()
