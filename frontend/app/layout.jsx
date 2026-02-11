import ThemeRegistry from './theme-registry';

export const metadata = {
  title: 'Medical Wiki',
  description: 'Medical knowledge base for diseases, symptoms, risk factors, and drugs.'
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <ThemeRegistry>{children}</ThemeRegistry>
      </body>
    </html>
  );
}
