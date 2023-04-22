'''TODO
1- Find a way to scroll in appbar
2- add parse section for APIs
3- Make the API models for each section
4- Correct the ImageField
'''



import flet
from flet import (Page, padding, ScrollMode, ThemeMode, TextAlign, alignment, Theme,
                Image,  WEB_BROWSER, ProgressBar, Container, 
                Column, Row, app, AppBar, Text, MainAxisAlignment,
                TextButton, ResponsiveRow, FontWeight, CrossAxisAlignment)





def main(page: Page):



    projectCard = Container(bgcolor='#2d7090', width=300, height=350, border_radius=10,
                        content=Column([Image(),
                                        Text(),
                                             ]))
    

    workCard = Container(bgcolor='#2d7090', width=300, height=350, border_radius=10,
                        content=Column([Image(),
                                        Text(),
                                             ]))


    skillBar = ResponsiveRow([
                            Text('test skill', color='white'),
                            ProgressBar(value=0.78),]) 

    aboutSection = Container(height=700, border_radius=0, bgcolor='#FF0f1530', 
                              content=Row(
                                controls=[Container(width=100),
                                    Column(controls=[
                                        Container(width=400),
                                        Text('ABOUT ME',color='#6335ff',size=15,weight=FontWeight.BOLD),
                                        Text('TEST', weight=FontWeight.W_600, color='white', size=40),
                                        Text('trsububub', color='#FFa2a2a2', size=13),
                                        Container()
                                    ], alignment=MainAxisAlignment.CENTER)
                                ]
                              ))

    welcomeSection = Container(padding=200, content=Text('test', color='White', size=40, text_align=TextAlign.CENTER), alignment=alignment.center)

    workSection = Container(border_radius=0, bgcolor='#0f1530',
                          alignment=alignment.top_center, 
                          content=Column(
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Container(margin=10),
                                    Text('WORK',color='#6335ff',size=15,weight=FontWeight.BOLD, text_align=TextAlign.CENTER),
                                    Text('TEST', weight=FontWeight.W_600, color='White', size=40),
                                    Container(margin=5),
                                    Container(bgcolor='#FF0f1530', height=450,
                                              content=Column(horizontal_alignment=CrossAxisAlignment.START,controls=[Container(margin=20), 
                                                        Row(spacing=70, scroll=ScrollMode.AUTO, opacity=0.7, 
                                                          controls=[Container(width=20, height=50),
                                                                    workCard,
                                                                    workCard,
                                                                    workCard,
                                                                    workCard,
                                                                    workCard,
                                                                    workCard,
                                                                    workCard,
                                                                    workCard,
                                                                    workCard,
                                                                    workCard,
                                                                    Container(width=20, height=50)]
                                                        )
                                                    ]
                                                )
                                            )
                                ]
                          )
                )


    projectSection =  Container(border_radius=0, bgcolor='#0f1530', 
                          alignment=alignment.top_center,
                          content=Column(
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Container(margin=10),
                                    Text('PROJECTS',color='#6335ff',size=15,weight=FontWeight.BOLD, text_align=TextAlign.CENTER),
                                    Text('TEST', weight=FontWeight.W_600, color='White', size=40),
                                    Container(margin=5),
                                    Container(bgcolor='#FF0f1530', height=450,
                                              content=Column(horizontal_alignment=CrossAxisAlignment.START,controls=[Container(margin=20), 
                                                        Row(spacing=70, scroll=ScrollMode.AUTO, opacity=0.7, 
                                                          controls=[Container(width=20, height=50),
                                                                    projectCard,
                                                                    projectCard,
                                                                    projectCard,
                                                                    projectCard,
                                                                    projectCard,
                                                                    projectCard,
                                                                    projectCard,
                                                                    projectCard,
                                                                    projectCard,
                                                                    Container(width=20, height=50)]
                                                        )
                                                    ]
                                                )
                                            )
                                ]
                          )
                )

    skillsSection = Container(border_radius=0, bgcolor='#0f1530', height=450, alignment=alignment.center, padding=40,
                               content=Column([
                                    Row([Text('SKILLS',color='#6335ff',size=15,weight=FontWeight.BOLD, text_align=TextAlign.CENTER)], alignment=MainAxisAlignment.CENTER),
                                    skillBar,
                                    skillBar,
                                    skillBar,
                                    skillBar,
                                    skillBar,
                               ]))

    contactSection = Container(border_radius=0, bgcolor='#0f1530', alignment=alignment.top_center, content=
                        Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Container(margin=10),
                                Text('CONTACT ME',color='#6335ff',size=15,weight=FontWeight.BOLD, text_align=TextAlign.CENTER),
                                Container(margin=5),
                                Container(bgcolor='#FF0f1530', height=300, content=Column(controls=[
                                        Container(width=20),
                                        Text('Wanna talk about a project or just say hi 👋', color='white'),
                                        Text('  Say Hello', italic=True, weight=FontWeight.BOLD, size=15, color='white'),
                                        Text('Email: ahicsjo@ft.sidh', color='white'),
                                        Text('Phone: 9872384732874', color='white'),
                                        TextButton(text="LinkedIn"),
                                        Text('  Find me in',weight=FontWeight.BOLD, size=15, color='white'),
                                        Text('ohasdcuhsodh', color='white'),
                                            ]
                                        )
                                    )
                                ]
                            )
                        )

    #AppBar ----------------------------------------------------------------
    page.appbar = AppBar(
        toolbar_height = 50,
        automatically_imply_leading=True,
        bgcolor="#6335ff",
        # center_title=True,
        # leading=Container(width=100),
        # title=Text('ARYAN DEHDASHTI', size=13, weight=FontWeight.W_500, color='white', selectable=False, font_family="Tahoma"),
        actions=[
        Row(
            spacing=4,
            alignment=MainAxisAlignment.CENTER,
            controls=[
                TextButton(content=Text(value='ABOUT', color='white', size=10, ref=aboutSection)),
                TextButton(content=Text(value='SKILL', color='white', size=10, ref=skillsSection)),
                TextButton(content=Text(value='WORK', color='white', size=10, ref=workSection)),
                TextButton(content=Text(value='CONTACT', color='white',size=10, ref=contactSection)),
                TextButton(content=Text(value='GitHub', color='white', size=15)),
                Container(width=80,)
            ]
        )
        ]
    )

    st = Column(
            controls=[
                welcomeSection,
                aboutSection,
                workSection,
                projectSection,
                skillsSection,
                contactSection,
            ],
            alignment=MainAxisAlignment.CENTER,
            )
        


    page.add(st)
    page.bgcolor = '#6335ff'
    page.padding = padding.symmetric(horizontal=0)
    page.scroll=ScrollMode.AUTO
    theme = Theme()
    theme.theme_mode = ThemeMode.DARK
    theme.page_transitions.android = "openUpwards"
    page.update()
if __name__ == '__main__':
    app(target=main, view=WEB_BROWSER, web_renderer="html", port=5548)