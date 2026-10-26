# Topic 12f: Windows Programming

**Syllabus:** Introduction to Windows programming - Win32, Microsoft Foundation Classes (MFC), Documents and views, Resources, Message handling in Windows; Simple Applications (in Windows): Scrolling, splitting views, docking toolbars, status bars, common dialogs; Advanced Windows Programming: Multiple Document Interface (MDI), Multithreading, Object linking and Embedding (OLE), Active X controls, Active Template Library (ATL), Network programming.

Q1. WinMain signature in Win32 is:
A. int main()
B. int WINAPI WinMain(HINSTANCE,HINSTANCE,LPSTR,int)
C. void start()
D. DWORD ThreadProc()
Correct Answer: B

Q2. First parameter of WinMain (hInstance) denotes:
A. Window handle
B. Command line
C. Application instance handle
D. Message ID
Correct Answer: C

Q3. nCmdShow in WinMain specifies:
A. Thread ID
B. Icon
C. Cursor
D. How window is to be shown
Correct Answer: D

Q4. Core Win32 message loop uses:
A. GetMessage-TranslateMessage-DispatchMessage
B. printf-scanf
C. malloc-free
D. open-close only
Correct Answer: A

Q5. GetMessage returns FALSE when:
A. On WM_PAINT
B. On WM_QUIT
C. On WM_CREATE
D. On WM_MOUSEMOVE
Correct Answer: B

Q6. Window procedure signature is:
A. void func()
B. int main(int)
C. LRESULT CALLBACK WndProc(HWND,UINT,WPARAM,LPARAM)
D. DWORD APIENTRY DllMain()
Correct Answer: C

Q7. Registering window class uses:
A. RegisterClassEx + WNDCLASSEX
B. CreatePen
C. SelectObject
D. BitBlt
Correct Answer: A

Q8. Creating main window uses:
A. fopen
B. malloc
C. printf
D. CreateWindowEx
Correct Answer: D

Q9. Message map equivalent in raw Win32 vs MFC:
A. Identical syntax
B. Switch-case on msg vs BEGIN_MESSAGE_MAP macros
C. No handling needed
D. Only BIOS interrupts
Correct Answer: B

Q10. DefWindowProc is used to:
A. Destroy app
B. Create thread
C. Provide default handling for unprocessed messages
D. Compile resources
Correct Answer: C

Q11. WM_CREATE is sent:
A. At window creation
B. At window destroy
C. On key press
D. On timer only
Correct Answer: A

Q12. WM_PAINT should be handled with:
A. malloc
B. CreateThread
C. socket
D. BeginPaint / EndPaint + HDC drawing
Correct Answer: D

Q13. Invalidating window to trigger repaint uses:
A. Sleep
B. InvalidateRect
C. WaitForSingleObject
D. RegOpenKey
Correct Answer: B

Q14. MFC application class derived from:
A. CWnd
B. CDocument
C. CWinApp
D. CView
Correct Answer: C

Q15. CWinApp::InitInstance typically:
A. Creates document template & main frame
B. Deletes OS
C. Formats disk
D. Installs driver
Correct Answer: A

Q16. Root of MFC hierarchy:
A. CWnd
B. CView
C. CWinApp
D. CObject
Correct Answer: D

Q17. CCmdTarget enables:
A. Drawing only
B. Message routing / command handling
C. Memory chip
D. Network cable
Correct Answer: B

Q18. CWnd encapsulates:
A. HWND + window operations
B. Only files
C. Only threads
D. Only database
Correct Answer: A

Q19. CFrameWnd vs CView:
A. Same
B. Both documents
C. Frame is container window; View displays document data
D. View is frame
Correct Answer: C

Q20. CDocument stores:
A. Pixels only
B. HWND only
C. Threads only
D. Application data + serialization
Correct Answer: D

Q21. Document/View separation benefit:
A. Faster CPU
B. Multiple views on same data (splitter, MDI)
C. No benefit
D. Larger exe only
Correct Answer: B

Q22. CWinApp message pump is in:
A. Run() with PreTranslateMessage
B. main() of C
C. BIOS
D. Bootloader
Correct Answer: A

Q23. AfxWinMain internally calls:
A. printf
B. scanf
C. InitInstance, Run
D. Format
Correct Answer: C

Q24. hPrevInstance in Win32 is:
A. Used heavily in Win32
B. Thread handle
C. File handle
D. Obsolete/NULL in Win32
Correct Answer: D

Q25. LPSTR lpCmdLine gives:
A. Window style
B. Command-line string
C. Icon
D. Menu
Correct Answer: B

Q26. WNDCLASSEX::lpfnWndProc holds:
A. Pointer to window procedure
B. Brush colour only
C. Thread ID
D. File path
Correct Answer: A

Q27. WS_OVERLAPPEDWINDOW style means:
A. Invisible
B. Child only
C. Standard titled, sizable window with sysmenu/min-max
D. Button only
Correct Answer: C

Q28. ShowWindow + UpdateWindow after CreateWindow to:
A. Delete window
B. Hide forever
C. Start thread
D. Display and force initial paint
Correct Answer: D

Q29. PostQuitMessage posts:
A. WM_QUIT
B. WM_PAINT
C. WM_CREATE
D. WM_CLOSE only
Correct Answer: A

Q30. GetMessage vs PeekMessage:
A. Same
B. GetMessage blocks; PeekMessage non-blocking (for games/idle)
C. Peek blocks more
D. GetMessage for DOS only
Correct Answer: B

Q31. MFC class CObject provides:
A. Windows
B. Sockets
C. Serialization, RTTI, diagnostics (DECLARE/IMPLEMENT_DYNAMIC)
D. Printing only
Correct Answer: C

Q32. CArchive works with:
A. Serialization (<< / >> with CDocument::Serialize)
B. Audio only
C. Video only
D. BIOS
Correct Answer: A

Q33. DECLARE_DYNCREATE enables:
A. Drawing
B. Threading
C. Networking
D. Runtime object creation by class name
Correct Answer: D

Q34. CDocument::OnNewDocument called when:
A. On exit
B. New file
C. On print
D. On help
Correct Answer: B

Q35. CDocument::Serialize loads/saves via:
A. CArchive
B. CWnd
C. CMenu
D. CThread
Correct Answer: A

Q36. CView::OnDraw receives:
A. HANDLE file
B. SOCKET
C. CDC*
D. HMENU
Correct Answer: C

Q37. CDC encapsulates:
A. Window handle
B. File
C. Thread
D. Device context (HDC)
Correct Answer: D

Q38. CPaintDC used:
A. Anywhere
B. Only in OnDraw/WM_PAINT
C. In threads only
D. In DllMain
Correct Answer: B

Q39. CClientDC used:
A. Drawing outside paint (e.g., mouse handlers)
B. Only for printing
C. Only for files
D. Only for registry
Correct Answer: A

Q40. Resource script file extension:
A. .cpp
B. .h
C. .rc
D. .exe
Correct Answer: C

Q41. Resource header for IDs:
A. resource.h
B. windows.exe
C. stdio.h
D. winsock.dll
Correct Answer: A

Q42. Dialog resource editor creates:
A. .exe
B. .obj
C. .lib
D. Dialog template + DoModal() via CDialog
Correct Answer: D

Q43. Modal vs Modeless dialog:
A. Same
B. Modal blocks (DoModal); modeless (Create/ShowWindow) allows parallel
C. Modeless blocks
D. Modal has no return
Correct Answer: B

Q44. DDX/DDV stands for:
A. Disk defrag
B. DirectX
C. Dialog Data Exchange/Validation
D. Data delete
Correct Answer: C

Q45. Message box API:
A. MessageBox / AfxMessageBox
B. printf
C. cout
D. Beep only
Correct Answer: A

Q46. Menu resource attached via:
A. malloc
B. free
C. new
D. LoadMenu / SetMenu + COMMAND handlers
Correct Answer: D

Q47. Accelerator table provides:
A. Faster CPU
B. Keyboard shortcuts (LoadAccelerators, TranslateAccelerator)
C. Faster disk
D. Faster network
Correct Answer: B

Q48. Icon/cursor resources loaded by:
A. fopen
B. CreateFile
C. LoadIcon / LoadCursor
D. socket
Correct Answer: C

Q49. Version resource stores:
A. Version, copyright info
B. Pixels
C. Threads
D. Packets
Correct Answer: A

Q50. String Table resource helps:
A. Obfuscation
B. Hardcode
C. Speed
D. Localization (LoadString)
Correct Answer: D

Q51. WM_COMMAND originates from:
A. Mouse move
B. Menu, button, accelerator
C. Paint
D. Timer only
Correct Answer: B

Q52. WM_NOTIFY vs WM_COMMAND:
A. Same
B. NOTIFY older
C. NOTIFY carries NMHDR with richer info for common controls
D. COMMAND for listview only
Correct Answer: C

Q53. MFC message map macro block:
A. BEGIN_MESSAGE_MAP … END_MESSAGE_MAP + ON_COMMAND/ON_WM_PAINT
B. begin-end
C. if-else only
D. switch in main
Correct Answer: A

Q54. ON_WM_PAINT maps to:
A. OnCreate
B. OnClose
C. OnQuit
D. OnPaint
Correct Answer: D

Q55. Command routing order MFC (MDI):
A. App first
B. View → Document → Frame → App
C. OS first
D. Random
Correct Answer: B

Q56. ON_UPDATE_COMMAND_UI used for:
A. Drawing
B. Threading
C. Enabling/disabling/checking menu/toolbar items
D. Deleting files
Correct Answer: C

Q57. PreTranslateMessage allows:
A. Filtering/translating accelerator/tooltip before dispatch
B. Compiling
C. Linking
D. Formatting disk
Correct Answer: A

Q58. Window messages WM_LBUTTONDOWN params:
A. Only HWND
B. Only MSG
C. Only HDC
D. x,y in LPARAM, flags in WPARAM
Correct Answer: D

Q59. Capturing mouse uses:
A. printf
B. SetCapture / ReleaseCapture
C. malloc
D. free
Correct Answer: B

Q60. Keyboard messages:
A. WM_PAINT
B. WM_TIMER
C. WM_KEYDOWN/WM_CHAR/WM_KEYUP
D. WM_QUIT only
Correct Answer: C

Q61. Scroll bar messages:
A. WM_HSCROLL/WM_VSCROLL with SB_* codes
B. WM_CREATE only
C. WM_DESTROY only
D. WM_QUIT only
Correct Answer: A

Q62. CScrollView provides:
A. No scroll
B. Only dialogs
C. Only threads
D. Automatic scroll handling (SetScrollSizes, OnInitialUpdate)
Correct Answer: D

Q63. SetScrollSizes parameters include:
A. Only colour
B. Map mode + total size + page/line size
C. Only font
D. Only icon
Correct Answer: B

Q64. Mapping modes (MM_TEXT, MM_LOenzi etc.) control:
A. Threads
B. Sockets
C. Logical-to-device coordinate conversion
D. File paths
Correct Answer: C

Q65. Splitter window class:
A. CSplitterWnd
B. CDialog
C. CMenu
D. CFile
Correct Answer: A

Q66. Static vs Dynamic splitter:
A. Same
B. No difference
C. Static for MDI only
D. Static fixed panes; dynamic allows split/unsplit at runtime
Correct Answer: D

Q67. CreateStatic / CreateView used in:
A. Dialogs
B. Splitter pane creation
C. Threads
D. Sockets
Correct Answer: B

Q68. Docking toolbar base class:
A. CView
B. CDocument
C. CToolBar / CControlBar
D. CWinApp
Correct Answer: C

Q69. EnableDocking + DockControlBar allows:
A. Draggable dockable toolbars
B. Fixed menus
C. No UI
D. Fullscreen only
Correct Answer: A

Q70. CStatusBar panes set via:
A. printf
B. malloc
C. socket
D. SetIndicators + SetPaneInfo/Text
Correct Answer: D

Q71. Rebar / dialog bar are:
A. File types
B. Extended control bars for combos/bands
C. Threads
D. Sockets
Correct Answer: B

Q72. Common dialog for open file:
A. CColorDialog
B. CFontDialog
C. CFileDialog(TRUE)
D. CPrintDialog only
Correct Answer: C

Q73. Save dialog uses:
A. CFileDialog(FALSE)
B. MessageBox
C. CWinApp
D. CView
Correct Answer: A

Q74. CFontDialog + LOGFONT selects:
A. File
B. Colour only
C. Printer only
D. Font
Correct Answer: D

Q75. CColorDialog returns:
A. File path
B. Chosen COLORREF
C. Font
D. Brush handle only
Correct Answer: B

Q76. CPrintDialog / Page Setup enables:
A. Network config
B. Thread config
C. Printing + device context setup
D. File delete
Correct Answer: C

Q77. Print preview in MFC uses:
A. OnFilePrintPreview (CPreviewView)
B. WinExec
C. ShellExecute only
D. Beep
Correct Answer: A

Q78. MDI frame classes:
A. CFrameWnd only
B. CDialog only
C. CView only
D. CMDIFrameWnd + CMDIChildWnd
Correct Answer: D

Q79. CMultiDocTemplate manages:
A. Single window only
B. Multiple document instances + frame/view linkage
C. Threads only
D. Sockets only
Correct Answer: B

Q80. Active MDI child handling via:
A. printf
B. malloc
C. MDIGetActive / MDIMaximize / MDINext
D. fopen
Correct Answer: C

Q81. SDI vs MDI:
A. SDI one document; MDI multiple children in parent frame
B. Same
C. SDI multiple, MDI single
D. No difference
Correct Answer: A

Q82. Tiling/cascading MDI children uses:
A. DrawText
B. BitBlt
C. CreateThread
D. MDITile / MDICascade
Correct Answer: D

Q83. Worker thread entry in MFC/Win32:
A. WinMain
B. ThreadProc / AfxBeginThread (UINT func(LPVOID))
C. WndProc
D. DllMain only
Correct Answer: B

Q84. UI thread has:
A. No pump
B. Only files
C. Message pump (CWinThread with PreTranslateMessage)
D. Only console
Correct Answer: C

Q85. Creating thread via Win32:
A. CreateThread
B. CreateWindow
C. CreateFile
D. CreateMenu
Correct Answer: A

Q86. Creating thread via MFC:
A. new only
B. malloc
C. fopen
D. AfxBeginThread
Correct Answer: D

Q87. Thread sync object for mutual exclusion:
A. HDC
B. Mutex / CriticalSection (CCriticalSection)
C. HWND
D. HMENU
Correct Answer: B

Q88. CriticalSection vs Mutex:
A. Same
B. Mutex inter-process, lighter CS intra-process (Enter/LeaveCriticalSection)
C. CS faster intra-process; mutex cross-process + ownership
D. CS for files only
Correct Answer: C

Q89. Event objects (CEvent) used for:
A. Signaling (SetEvent/WaitForSingleObject)
B. Drawing
C. Printing
D. Filing
Correct Answer: A

Q90. Semaphore limits:
A. One thread only always
B. No limit
C. For UI only
D. Counted concurrent access (CSemaphore)
Correct Answer: D

Q91. Deadlock occurs when:
A. No sync
B. Circular wait on locks
C. Fast code
D. No threads
Correct Answer: B

Q92. Interlocked functions provide:
A. File IO
B. Window draw
C. Atomic ops (InterlockedIncrement)
D. Socket connect
Correct Answer: C

Q93. PostThreadMessage vs PostMessage:
A. To thread queue vs window queue
B. Same
C. To file
D. To printer
Correct Answer: A

Q94. Thread local storage (TLS) is for:
A. Shared global
B. Window text
C. Menu
D. Per-thread data (TlsAlloc/SetValue)
Correct Answer: D

Q95. Terminating thread safely:
A. TerminateThread always
B. Return / exit + WaitForSingleObject; avoid force-kill
C. Pull plug
D. Delete file
Correct Answer: B

Q96. Suspend/Resume thread APIs:
A. Show/Hide
B. Open/Close
C. SuspendThread / ResumeThread
D. Play/Pause media only
Correct Answer: C

Q97. OLE full form:
A. Object Linking and Embedding
B. Online Event
C. Open Link Engine
D. Object List Editor
Correct Answer: A

Q98. Linked vs Embedded OLE object:
A. Same
B. Both static
C. No difference
D. Linked references external; embedded stores copy inside container
Correct Answer: D

Q99. OLE container vs server:
A. Same
B. Container hosts; server provides object (e.g., Word in MFC app)
C. Server hosts
D. Container provides
Correct Answer: B

Q100. COM foundation for OLE/ActiveX uses:
A. Plain text
B. printf
C. IUnknown (QueryInterface/AddRef/Release) + GUIDs
D. Batch files
Correct Answer: C

Q101. COleDocument / COleClientItem support:
A. Compound documents with embedded items
B. Only text files
C. Only threads
D. Only sockets
Correct Answer: A

Q102. In-place activation allows:
A. Separate window only
B. No editing
C. Print only
D. Edit server object inside container UI (menus merge)
Correct Answer: D

Q103. ActiveX control is:
A. DOS program
B. COM-based reusable UI/control (OCX) with properties/methods/events
C. Image file
D. Text file
Correct Answer: B

Q104. ActiveX container (MFC dialog) hosts via:
A. printf
B. malloc
C. Wrapper class from typelibrary + properties/methods
D. fopen
Correct Answer: C

Q105. IDispatch enables:
A. Late binding automation (Invoke)
B. Early binding only
C. Static linking only
D. No scripting
Correct Answer: A

Q106. ATL stands for:
A. Advanced Text Library
B. Audio Tape Library
C. Auto Thread Locker
D. Active Template Library
Correct Answer: D

Q107. ATL advantage vs MFC for COM:
A. Larger
B. Lightweight template-based, no heavy runtime
C. No COM
D. Only for GUI
Correct Answer: B

Q108. ATL macros BEGIN_COM_MAP defines:
A. Message map
B. Thread map
C. Interface map (QueryInterface entries)
D. Menu map
Correct Answer: C

Q109. CComModule / CComPtr help with:
A. Module registration + smart COM pointers (ref counting)
B. Drawing
C. Filing
D. Printing
Correct Answer: A

Q110. IDL file defines:
A. Window layout
B. Menu
C. Bitmap
D. COM interfaces/type library (MIDL compiles)
Correct Answer: D

Q111. Registering COM server uses:
A. printf
B. regsvr32 / DllRegisterServer
C. copy/paste
D. reboot only
Correct Answer: B

Q112. Apartments (STA/MTA) relate to:
A. Housing
B. Files
C. COM threading model (CoInitialize/CoInitializeEx)
D. Windows size
Correct Answer: C

Q113. Marshaling in COM is for:
A. Cross-apartment/process parameter passing
B. Drawing lines
C. Filing papers
D. Printing pages
Correct Answer: A

Q114. Connection points in ActiveX provide:
A. Power plugs
B. Network cables
C. File handles
D. Events/callbacks to container (sinks)
Correct Answer: D

Q115. MFC OLE init requires:
A. printf
B. AfxOleInit()
C. malloc
D. fopen
Correct Answer: B

Q116. Network programming base API on Windows:
A. BIOS
B. DOS
C. Winsock (WSAStartup, sockets)
D. PRINT
Correct Answer: C

Q117. WSAStartup negotiates:
A. Winsock version (e.g., 2.2)
B. Window size
C. Font
D. Colour
Correct Answer: A

Q118. TCP socket sequence (server):
A. connect-send-close only
B. bind only
C. listen only
D. socket-bind-listen-accept-send/recv-closesocket
Correct Answer: D

Q119. TCP vs UDP:
A. Same
B. TCP reliable connection-oriented; UDP datagram unreliable/fast
C. UDP reliable
D. TCP datagram
Correct Answer: B

Q120. getaddrinfo / gethostbyname used for:
A. Drawing
B. Printing
C. Hostname→IP resolution
D. File delete
Correct Answer: C

Q121. htons/ntohl convert:
A. Host↔network byte order
B. Text to image
C. Font sizes
D. Colours
Correct Answer: A

Q122. CSocket / CAsyncSocket MFC classes wrap:
A. Files
B. Windows
C. Menus
D. Winsock with message-driven callbacks (OnReceive/OnAccept)
Correct Answer: D

Q123. Blocking vs Non-blocking sockets:
A. Same
B. Blocking waits; non-blocking + select/WSAAsyncSelect returns immediately
C. Non-blocking waits more
D. Blocking for UDP only
Correct Answer: B

Q124. select() allows:
A. Drawing choice
B. Menu choice
C. Multiplexing / waiting on multiple sockets
D. Font choice
Correct Answer: C

Q125. Overlapped IO / IOCP provides:
A. Scalable async network IO
B. Sync file delete
C. Sync draw
D. Sync print
Correct Answer: A

Q126. HTTP programming can use:
A. Only sockets raw always
B. Only MFC draw
C. Only BIOS
D. WinInet/WinHTTP (InternetOpen, HttpOpenRequest) or sockets
Correct Answer: D

Q127. WNDPROC hook vs subclassing:
A. Same as painting
B. Intercept/override window messages (SetWindowLong)
C. File hook
D. Thread hook only
Correct Answer: B

Q128. GDI object for lines:
A. CBrush
B. CFont
C. CPen
D. CBitmap
Correct Answer: C

Q129. GDI object for fills:
A. CBrush
B. CPen
C. CFont
D. CPalette only
Correct Answer: A

Q130. Device contexts memory (off-screen) uses:
A. Beep
B. Sleep
C. Wait
D. CreateCompatibleDC + CreateCompatibleBitmap (double buffering)
Correct Answer: D

Q131. BitBlt / StretchBlt do:
A. Delete files
B. Fast bitmap block transfer (with scaling for Stretch)
C. Send packets
D. Create threads
Correct Answer: B

Q132. WM_TIMER handling uses:
A. malloc
B. socket
C. SetTimer/KillTimer + OnTimer
D. fopen
Correct Answer: C

Q133. Modeless dialog creation:
A. Create + ShowWindow (+ DestroyWindow)
B. DoModal only
C. MessageBox only
D. WinExec
Correct Answer: A

Q134. EndDialog vs DestroyWindow:
A. Same
B. Both for modeless
C. Both for threads
D. EndDialog for modal; DestroyWindow for modeless
Correct Answer: D

Q135. CListCtrl view modes:
A. Only icon
B. Icon, Report, List, SmallIcon
C. Only text
D. Only bitmap
Correct Answer: B

Q136. CTreeCtrl nodes use:
A. Pixels
B. Packets
C. HTREEITEM + TVINSERTSTRUCT
D. Threads
Correct Answer: C

Q137. PropertySheet/Page (CPropertySheet) implements:
A. Tabbed dialogs
B. Menus only
C. Toolbars only
D. Sockets
Correct Answer: A

Q138. DIB vs DDB:
A. Same
B. Both printers
C. Both files
D. Device-independent vs device-dependent bitmap
Correct Answer: D

Q139. OnEraseBkgnd returning TRUE means:
A. Error
B. Background handled (avoid flicker)
C. Repaint always
D. Exit app
Correct Answer: B

Q140. Double buffering avoids:
A. Network lag
B. Disk lag
C. Flicker
D. Thread lag
Correct Answer: C

Q141. File open dialog filter string format:
A. "Text (*.txt)|*.txt||"
B. Plain sentence
C. Only "*.*"
D. No format
Correct Answer: A

Q142. CWinApp::ExitInstance cleans:
A. Nothing
B. Only windows
C. Only menus
D. App cleanup (GDI, sockets, threads)
Correct Answer: D

Q143. AfxGetApp / AfxGetMainWnd return:
A. HDC/HWND only
B. App object / main window pointers
C. Files
D. Sockets
Correct Answer: B

Q144. ASSERT vs VERIFY in MFC:
A. Same release
B. Both ignored
C. ASSERT debug-only; VERIFY evaluates in release too
D. Both for release
Correct Answer: C

Q145. Unicode (TCHAR, _T) handling:
A. Portable ANSI/Unicode builds (use LPCTSTR, _T)
B. Only ANSI
C. Only ASCII art
D. No text
Correct Answer: A

Q146. DLL entry for MFC extension DLL:
A. WinMain
B. main
C. ThreadProc
D. DllMain + AFX_MANAGE_STATE
Correct Answer: D

Q147. AFX_MANAGE_STATE needed to:
A. Draw faster
B. Switch module state for MFC DLL resources
C. Speed network
D. Manage threads only
Correct Answer: B

Q148. Mass virtual functions OnDraw/Serialize show:
A. No polymorphism
B. Overloading only
C. MFC document/view polymorphism
D. Templates only
Correct Answer: C

Q149. Message reflection (ON_NOTIFY_REFLECT) is for:
A. Let control handle its own notifications (e.g., custom draw)
B. Mirror display
C. Network echo
D. Thread echo
Correct Answer: A

Q150. Custom control drawing via:
A. Beep
B. Sleep
C. Wait
D. WM_DRAWITEM / OnDrawItem + owner-draw
Correct Answer: D

Q151. Timer vs Multithreading for background:
A. Same
B. Timer for light UI periodic; threads for heavy/parallel
C. Timer for heavy
D. Threads for UI only
Correct Answer: B

Q152. Worker thread must not directly:
A. Compute
B. Read file
C. Touch UI (use PostMessage)
D. Allocate memory
Correct Answer: C

Q153. SendMessage vs PostMessage:
A. Send synchronous (waits); Post async (queues)
B. Same
C. Post waits
D. Send queues only
Correct Answer: A

Q154. CriticalSection MFC wrapper:
A. CWinApp
B. CView
C. CDoc
D. CCriticalSection + CSingleLock
Correct Answer: D

Q155. CMutex vs CCriticalSection scope:
A. Same machine only both
B. Mutex named cross-process; CS intra-process
C. CS cross-process
D. Mutex intra only
Correct Answer: B

Q156. CEvent auto vs manual reset:
A. Same
B. No difference
C. Auto resets after one waiter; manual stays signaled till ResetEvent
D. Both manual
Correct Answer: C

Q157. WaitForMultipleObjects waits on:
A. Multiple handles
B. One pixel
C. One file
D. One menu
Correct Answer: A

Q158. UI update from worker via:
A. Direct CDC
B. Direct CWnd
C. malloc
D. PostMessage custom WM_USER+n
Correct Answer: D

Q159. Thread priority via:
A. ShowWindow
B. SetThreadPriority
C. SetWindowText
D. SetMenu
Correct Answer: B

Q160. OnIdle processing in MFC:
A. Never
B. Only for games
C. CWinApp::OnIdle for background UI updates
D. Only for drivers
Correct Answer: C

Q161. SDI template class:
A. CSingleDocTemplate
B. CMultiDocTemplate
C. CDialogTemplate
D. CThreadTemplate
Correct Answer: A

Q162. DocTemplate resources link:
A. Random
B. Only code
C. Only data
D. IDR_MAINFRAME (menu, icon, accel) + doc/view/frame classes
Correct Answer: D

Q163. RUNTIME_CLASS macro provides:
A. Compile-time only
B. Runtime class info for dynamic creation
C. Static text
D. Menu
Correct Answer: B

Q164. IMPLEMENT_DYNCREATE in .cpp pairs with:
A. BEGIN_MESSAGE_MAP
B. malloc
C. DECLARE_DYNCREATE in header
D. #include only
Correct Answer: C

Q165. View initial update via:
A. OnInitialUpdate
B. OnDraw only
C. OnCreate only
D. WinMain
Correct Answer: A

Q166. Document modified flag:
A. No flag
B. Only file date
C. Only read-only
D. SetModifiedFlag + IsModified for save prompt
Correct Answer: D

Q167. File MRU list handled by:
A. Manual code only
B. CWinApp MRU (LoadStdProfileSettings, AddToRecentFileList)
C. BIOS
D. Boot ini
Correct Answer: B

Q168. Registry vs INI for settings:
A. Same speed always
B. INI for large data
C. Registry (SetRegistryKey) structured; INI legacy files
D. No settings
Correct Answer: C

Q169. Help context (F1) uses:
A. Help IDs + WinHelp/HTML Help
B. printf
C. Beep
D. MessageBox only
Correct Answer: A

Q170. Drag-drop files (WM_DROPFILES) needs:
A. No setup
B. Only menu
C. Only thread
D. DragAcceptFiles + HDROP handling
Correct Answer: D

Q171. Clipboard (OpenClipboard/SetClipboardData) shares:
A. Threads
B. Data across apps (CF_TEXT, CF_BITMAP)
C. Files only
D. Sockets
Correct Answer: B

Q172. Drag-drop OLE (COleDropSource/Target) enables:
A. File delete
B. Window move only
C. Rich drag-drop with formats
D. Text only
Correct Answer: C

Q173. Shell execute to open doc:
A. ShellExecute / CreateProcess
B. malloc
C. free
D. BitBlt
Correct Answer: A

Q174. Process vs Thread:
A. Same
B. Thread has own address space
C. Process lightweight
D. Process isolated space; thread shares within process
Correct Answer: D

Q175. CreateProcess parameters include:
A. Only exe name
B. App name, cmdline, security, creation flags, STARTUPINFO
C. Only icon
D. Only menu
Correct Answer: B

Q176. Named pipes (CreateNamedPipe) for:
A. Drawing
B. Printing only
C. IPC (local/remote byte streams)
D. Filing only
Correct Answer: C

Q177. Mailslots vs Pipes:
A. Mailslots one-way broadcast; pipes two-way reliable
B. Same
C. Pipes broadcast
D. Mailslots two-way
Correct Answer: A

Q178. Winsock cleanup via:
A. closesocket only
B. close()
C. ExitProcess
D. WSACleanup
Correct Answer: D

Q179. socket() params:
A. HWND,MSG
B. af, type, protocol (e.g., AF_INET,SOCK_STREAM)
C. HDC only
D. HMENU only
Correct Answer: B

Q180. bind() associates:
A. Window to class
B. Thread to CPU
C. Socket to IP/port
D. Menu to window
Correct Answer: C

Q181. listen() + accept() do:
A. Queue + accept incoming TCP connections
B. Draw + paint
C. Open + save
D. Send + recv only
Correct Answer: A

Q182. connect() is used by:
A. Server only
B. Printer only
C. Plotter only
D. Client to reach server
Correct Answer: D

Q183. send()/recv() vs WSASend/Recv:
A. Same always
B. Basic vs overlapped-capable ex versions
C. No difference
D. Only for UDP
Correct Answer: B

Q184. closesocket() should be paired with:
A. CloseWindow
B. DeleteFile
C. Earlier socket() + shutdown() for graceful
D. DestroyMenu
Correct Answer: C

Q185. gethostname + inet_addr handle:
A. Name/IP conversion
B. Font conversion
C. Colour conversion
D. Menu conversion
Correct Answer: A

Q186. Firewall-friendly COM (DCOM) uses:
A. Only files
B. Only local
C. No network
D. RPC + CoCreateInstanceEx for remote objects
Correct Answer: D

Q187. Apartment init for UI thread with COM:
A. No init
B. CoInitialize (STA) + message pump
C. Only MTA
D. Only files
Correct Answer: B

Q188. BSTR vs CString:
A. Same
B. Both narrow
C. BSTR COM length-prefixed wide; CString MFC wrapper (convert via _bstr_t/CComBSTR)
D. Both for files
Correct Answer: C

Q189. HRESULT S_OK means:
A. Success
B. Failure
C. Pending
D. Cancelled
Correct Answer: A

Q190. ActiveX signing (Authenticode) ensures:
A. Faster load
B. Smaller size
C. Better UI
D. Trust/origin for safe download (reduce warnings)
Correct Answer: D

Q191. ATL vs MFC footprint reminder:
A. ATL heavier
B. ATL minimal (no document/view bloat) ideal for controls/servers
C. MFC minimal
D. Same
Correct Answer: B

Q192. Dual interface (IDispatch + vtable) allows:
A. Only C++
B. Only script
C. Both early (fast C++) + late (VB/script) binding
D. Neither
Correct Answer: C

Q193. Type library (.tlb) generated from:
A. IDL via MIDL
B. .rc via rc.exe
C. .cpp via cl.exe only
D. .bmp via paint
Correct Answer: A

Q194. Proxy/stub DLL handles:
A. Drawing
B. Printing
C. Filing
D. Marshaling for custom interfaces
Correct Answer: D

Q195. Common control init needs:
A. printf
B. InitCommonControlsEx
C. malloc
D. fopen
Correct Answer: B

Q196. Tooltip support via:
A. No code
B. Only menus
C. EnableToolTips + ON_NOTIFY(TTN_)
D. Only dialogs modal
Correct Answer: C

Q197. Win32 error via:
A. GetLastError + FormatMessage
B. errno only
C. printf only
D. Beep
Correct Answer: A

Q198. Debug output via:
A. printf to console always
B. cout only
C. MessageBox only
D. OutputDebugString + TRACE macro
Correct Answer: D

Q199. High-DPI awareness needs:
A. Ignore
B. Manifest + GetDpiForWindow / scaling
C. Larger fonts only
D. Smaller windows
Correct Answer: B

Q200. Best practice for MFC/Win32 app shutdown:
A. Kill process
B. Pull plug
C. Close documents (SaveModified), destroy windows, cleanup GDI/sockets/threads, PostQuitMessage
D. Delete exe  ---
Correct Answer: C

---
## ANSWER KEY
1-B 2-C 3-D 4-A 5-B 6-C 7-A 8-D 9-B 10-C
11-A 12-D 13-B 14-C 15-A 16-D 17-B 18-A 19-C 20-D
21-B 22-A 23-C 24-D 25-B 26-A 27-C 28-D 29-A 30-B
31-C 32-A 33-D 34-B 35-A 36-C 37-D 38-B 39-A 40-C
41-A 42-D 43-B 44-C 45-A 46-D 47-B 48-C 49-A 50-D
51-B 52-C 53-A 54-D 55-B 56-C 57-A 58-D 59-B 60-C
61-A 62-D 63-B 64-C 65-A 66-D 67-B 68-C 69-A 70-D
71-B 72-C 73-A 74-D 75-B 76-C 77-A 78-D 79-B 80-C
81-A 82-D 83-B 84-C 85-A 86-D 87-B 88-C 89-A 90-D
91-B 92-C 93-A 94-D 95-B 96-C 97-A 98-D 99-B 100-C
101-A 102-D 103-B 104-C 105-A 106-D 107-B 108-C 109-A 110-D
111-B 112-C 113-A 114-D 115-B 116-C 117-A 118-D 119-B 120-C
121-A 122-D 123-B 124-C 125-A 126-D 127-B 128-C 129-A 130-D
131-B 132-C 133-A 134-D 135-B 136-C 137-A 138-D 139-B 140-C
141-A 142-D 143-B 144-C 145-A 146-D 147-B 148-C 149-A 150-D
151-B 152-C 153-A 154-D 155-B 156-C 157-A 158-D 159-B 160-C
161-A 162-D 163-B 164-C 165-A 166-D 167-B 168-C 169-A 170-D
171-B 172-C 173-A 174-D 175-B 176-C 177-A 178-D 179-B 180-C
181-A 182-D 183-B 184-C 185-A 186-D 187-B 188-C 189-A 190-D
191-B 192-C 193-A 194-D 195-B 196-C 197-A 198-D 199-B 200-C
