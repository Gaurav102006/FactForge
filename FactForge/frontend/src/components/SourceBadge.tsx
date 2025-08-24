
import React from 'react'

export default function SourceBadge({ title, url, publisher }:{ title:string, url:string, publisher?:string }){
  return (
    <a className="badge" href={url} target="_blank" rel="noreferrer" title={publisher || ''}>
      {title}
    </a>
  )
}
