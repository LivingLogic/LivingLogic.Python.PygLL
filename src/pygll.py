from pygments import token, style


class LivingLogicLightStyle(style.Style):
	"""
	The 'LivingLogic' style, light version
	"""

	# overall background color (``None`` means transparent)
	background_color = '#00000003'

	# highlight background color
	highlight_color = '#0f02'

	# line number font color
	line_number_color = '#7f7f7f'

	# line number background color
	line_number_background_color = 'transparent'

	# special line number font color
	line_number_special_color = '#666'

	# special line number background color
	line_number_special_background_color = 'transparent'

	styles = {
		token.Token:                '#191919',
		token.Generic.Output:       '#7f7f7f',
		token.Generic.Prompt:       '#ccc',
		token.Generic.Error:        '#ff1c1c',
		token.Generic.Traceback:    '#ff1c1c',
		token.Comment:              '#4c4c4c',
		token.Number:               '#cc00cb',
		token.String:               '#2b0',
		token.String.Doc:           '#416739',
		token.String.Interpol:      '#147000',
		token.String.Delimiter:     '#147000',
		token.String.Escape:        '#147000',
		token.String.Affix:         '#147000',
		token.Token.Literal.Date:   '#235757',
		token.Token.Literal.Color:  '#235757',
		token.Keyword:              '#05f',
		token.Keyword.Reserved:     '#af0d00',
		token.Operator:             '#05f',
		token.Operator.Word:        '#05f',
		token.Keyword.Constant:     '#774600',
		token.Name:                 '#191919',
		token.Name.Class:           '#191919 bold',
		token.Name.Function:        '#191919 bold',
		token.Name.Namespace:       '#191919',
		token.Name.Builtin.Pseudo:  '#102d65',
		token.Name.Variable.Magic:  '#102d65',
		token.Name.Function.Magic:  '#102d65',
		token.Name.Tag:             '#993d00',
		token.Name.Attribute:       '#232b0e',
		token.Name.Entity:          '#e700e6',
		token.Comment.Preproc:      '#006061',
		token.Token.Prompt:         '#00b200',
		token.Token.PromptNum:      '#006a00',
		token.Token.OutPrompt:      '#ff5d5d',
		token.Token.OutPromptNum:   '#ff1c1c',
	}


class LivingLogicDarkStyle(style.Style):
	"""
	The 'LivingLogic' style, dark version
	"""

	# overall background color (``None`` means transparent)
	background_color = '#ffffff03'

	# highlight background color
	highlight_color = '#030'

	# line number font color
	line_number_color = '#7f7f7f'

	# line number background color
	line_number_background_color = 'transparent'

	# special line number font color
	line_number_special_color = '#999'

	# special line number background color
	line_number_special_background_color = 'transparent'

	styles = {
		token.Token:                '#e5e5e5',
		token.Generic.Output:       '#999',
		token.Generic.Prompt:       '#656565',
		token.Generic.Error:        '#ff9d9d',
		token.Generic.Traceback:    '#ff9d9d',
		token.Comment:              '#b2b2b2',
		token.Number:               '#eb9beb',
		token.String:               '#a4c240',
		token.String.Doc:           '#aeb695',
		token.String.Interpol:      '#d1e09f',
		token.String.Delimiter:     '#d1e09f',
		token.String.Escape:        '#d1e09f',
		token.String.Affix:         '#d1e09f',
		token.Token.Literal.Date:   '#51cccc',
		token.Token.Literal.Color:  '#51cccc',
		token.Keyword:              '#80bce2',
		token.Keyword.Reserved:     '#dfa985',
		token.Operator:             '#80bce2',
		token.Operator.Word:        '#80bce2',
		token.Keyword.Constant:     '#ffa929',
		token.Name:                 '#e5e5e5',
		token.Name.Class:           '#e5e5e5 bold',
		token.Name.Function:        '#e5e5e5 bold',
		token.Name.Namespace:       '#e5e5e5',
		token.Name.Builtin.Pseudo:  '#c3d7e4',
		token.Name.Variable.Magic:  '#c3d7e4',
		token.Name.Function.Magic:  '#c3d7e4',
		token.Name.Tag:             '#ffa366',
		token.Name.Attribute:       '#dac992',
		token.Name.Entity:          '#eb9beb',
		token.Comment.Preproc:      '#00e2e2',
		token.Token.Prompt:         '#00b200',
		token.Token.PromptNum:      '#00f900',
		token.Token.OutPrompt:      '#ff5d5d',
		token.Token.OutPromptNum:   '#ff9d9d',
	}
