type SourceBadgeProps = {
  title: string
  url: string
  publisher?: string
}

export default function SourceBadge({ title, url, publisher }: SourceBadgeProps) {
  return (
    <a
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      className="px-3 py-1 bg-gray-200 hover:bg-gray-300 text-sm rounded-lg transition"
    >
      {title} {publisher && <span className="text-gray-500">({publisher})</span>}
    </a>
  )
}
