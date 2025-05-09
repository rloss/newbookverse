import './globals.css'
import Topbar from '../components/layout/Topbar'
import RightSidebar from '../components/layout/RightSidebar'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ko">
      <body className="flex flex-col h-screen">
        <Topbar />
        <div className="flex flex-1 overflow-hidden">
          <main className="flex-1 overflow-y-auto p-6">{children}</main>
          <RightSidebar />
        </div>
      </body>
    </html>
  )
}

