///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	m_menubar1 = new wxMenuBar( 0 );
	m_menu1 = new wxMenu();
	wxMenuItem* m_file_exit;
	m_file_exit = new wxMenuItem( m_menu1, wxID_ANY, wxString( wxT("Ex&it") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu1->Append( m_file_exit );

	m_menubar1->Append( m_menu1, wxT("&File") );

	m_menu2 = new wxMenu();
	wxMenuItem* m_help_about;
	m_help_about = new wxMenuItem( m_menu2, wxID_ANY, wxString( wxT("About") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu2->Append( m_help_about );

	wxMenuItem* m_help_tafe;
	m_help_tafe = new wxMenuItem( m_menu2, wxID_ANY, wxString( wxT("TAFE OS") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu2->Append( m_help_tafe );

	m_menubar1->Append( m_menu2, wxT("Help") );

	this->SetMenuBar( m_menubar1 );

	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxHORIZONTAL );

	wxGridSizer* gSizer2;
	gSizer2 = new wxGridSizer( 0, 2, 0, 0 );

	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("Host"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	gSizer2->Add( m_staticText1, 0, wxALL, 5 );

	host_text = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer2->Add( host_text, 0, wxALL, 5 );

	port_start_text = new wxStaticText( this, wxID_ANY, wxT("Start Port"), wxDefaultPosition, wxDefaultSize, 0 );
	port_start_text->Wrap( -1 );
	gSizer2->Add( port_start_text, 0, wxALL, 5 );

	m_textCtrl2 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer2->Add( m_textCtrl2, 0, wxALL, 5 );

	port_end_text = new wxStaticText( this, wxID_ANY, wxT("End Port"), wxDefaultPosition, wxDefaultSize, 0 );
	port_end_text->Wrap( -1 );
	gSizer2->Add( port_end_text, 0, wxALL, 5 );

	m_textCtrl3 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer2->Add( m_textCtrl3, 0, wxALL, 5 );

	threads_text = new wxStaticText( this, wxID_ANY, wxT("Threads"), wxDefaultPosition, wxDefaultSize, 0 );
	threads_text->Wrap( -1 );
	gSizer2->Add( threads_text, 0, wxALL, 5 );

	m_textCtrl4 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer2->Add( m_textCtrl4, 0, wxALL, 5 );


	bSizer1->Add( gSizer2, 1, wxEXPAND, 5 );

	wxStaticBoxSizer* sbSizer1;
	sbSizer1 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Open Ports") ), wxVERTICAL );

	ports_list = new wxListBox( sbSizer1->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxSize( -1,-1 ), 0, NULL, wxLB_SINGLE );
	sbSizer1->Add( ports_list, 5, wxALL|wxEXPAND, 5 );


	bSizer1->Add( sbSizer1, 1, wxEXPAND, 5 );


	this->SetSizer( bSizer1 );
	this->Layout();
	m_statusBar2 = this->CreateStatusBar( 1, wxSTB_SIZEGRIP, wxID_ANY );

	this->Centre( wxBOTH );
}

MyFrame1::~MyFrame1()
{
}
