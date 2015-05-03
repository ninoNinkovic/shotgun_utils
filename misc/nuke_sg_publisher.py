class Publisher(object):

	def CreateNode():
		n = nuke.createNode( 'NoOp' )
		sequence = nuke.Int_Knob('shot_field', 'Shot')
		shot_code = nuke.String_Knob('shot_code', 'Shot Code')
		sequence_source_path = nuke.File_Knob('seq_source', 'Sequence Sorce Folder')

		n.addKnob(sequence)
		n.addKnob(shot_code)
		n.addKnob(sequence_source_path)

		n['name'].setValue('SG Publish')
		n['shot_field'].setValue(001)
		n['shot_code'].setValue('BB_001_010')
		n['seq_source'].setValue('H:/Event_Version 1_0001_0001')